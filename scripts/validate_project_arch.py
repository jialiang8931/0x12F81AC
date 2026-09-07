from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT_FILES = frozenset({".gitignore", "AGENTS.md", "README.md", "SKILL.md"})
COMMON_PATHS = (
    "docs/init.md",
    "AGENTS.md",
    ".gitignore",
    "contracts/architecture.md",
    "contracts/business-init.md",
    "contracts/code-standards.md",
    "contracts/git-workflow.md",
    "contracts/testing.md",
    "contracts/writing-style.md",
    "tasks/README.md",
)
SERVICE_PATHS = (
    "contracts/dependency-management.md",
    "contracts/docker-lifecycle.md",
    "contracts/environment-files.md",
    "contracts/input-contract.md",
    "contracts/script-entrypoints.md",
    "infra/docker/Dockerfile",
    "infra/docker/Dockerfile.dockerignore",
    "scripts/manifest.json",
)
DEPLOYABLE_PATHS = ("contracts/deployment.md", "infra/terraform")
INIT_HEADINGS = (
    "業務問題",
    "使用者與利害關係人",
    "範圍與非範圍",
    "領域詞彙",
    "業務規則",
    "行為情境",
    "輸入與輸出",
    "驗收條件",
    "風險",
    "未決事項",
)


@dataclass(frozen=True)
class ValidationResult:
    errors: tuple[str, ...]

    @property
    def passed(self) -> bool:
        return not self.errors


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    closing = text.find("\n---\n", 4)
    if closing < 0:
        return {}
    pairs = (
        line.split(":", 1)
        for line in text[4:closing].splitlines()
        if ":" in line
    )
    return {key.strip(): value.strip().strip('"\'') for key, value in pairs}


def validate_business_init(path: Path) -> tuple[str, ...]:
    if not path.is_file() or path.is_symlink():
        return ("docs/init.md must be an existing regular file",)
    text = path.read_text(encoding="utf-8")
    metadata = parse_front_matter(text)
    owner = metadata.get("business_owner", "").strip().lower()
    errors = []
    if metadata.get("status") != "READY_FOR_GOVERNANCE":
        errors.append("docs/init.md status must be READY_FOR_GOVERNANCE")
    if not owner or owner in {"ai", "codex", "chatgpt", "assistant"}:
        errors.append("docs/init.md requires a human or domain business_owner")
    errors.extend(
        f"docs/init.md is missing heading: {heading}"
        for heading in INIT_HEADINGS
        if not re.search(rf"^#+\s+{re.escape(heading)}\s*$", text, re.MULTILINE)
    )
    if not (("Given" in text and "When" in text and "Then" in text) or
            ("假設" in text and "當" in text and "那麼" in text)):
        errors.append("docs/init.md requires at least one Given/When/Then scenario")
    if re.search(r"\b(?:TODO|TBD)\b|<[^>]+>", text, re.IGNORECASE):
        errors.append("docs/init.md contains unresolved placeholders")
    return tuple(errors)


def required_paths(profile: str) -> tuple[str, ...]:
    additions = SERVICE_PATHS if profile in {"service", "deployable"} else ()
    deployment = DEPLOYABLE_PATHS if profile == "deployable" else ()
    return COMMON_PATHS + additions + deployment


def validate_manifest(root: Path) -> tuple[str, ...]:
    path = root / "scripts/manifest.json"
    if not path.is_file():
        return ()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return (f"scripts/manifest.json is invalid: {error}",)
    entries = data.get("public_entrypoints", [])
    paths = [entry.get("path", "") for entry in entries if isinstance(entry, dict)]
    errors = [f"manifest entry does not exist: {item}" for item in paths if not (root / item).is_file()]
    if len(paths) != len(set(paths)):
        errors.append("scripts/manifest.json contains duplicate paths")
    return tuple(errors)


def validate_project(root: Path, profile: str) -> ValidationResult:
    resolved = root.resolve()
    errors = list(validate_business_init(resolved / "docs/init.md"))
    errors.extend(
        f"required path is missing: {item}"
        for item in required_paths(profile)
        if not (resolved / item).exists()
    )
    root_files = {item.name for item in resolved.iterdir() if item.is_file()}
    errors.extend(
        f"root-level file is not allowed: {item}"
        for item in sorted(root_files - ROOT_FILES)
    )
    if profile in {"service", "deployable"}:
        errors.extend(validate_manifest(resolved))
    return ValidationResult(tuple(errors))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--profile", choices=("docs-only", "service", "deployable"), required=True)
    args = parser.parse_args()
    result = validate_project(args.project_root, args.profile)
    if result.passed:
        print(f"PASSED: {args.profile} governance is structurally valid")
        return 0
    for error in result.errors:
        print(f"FAILED: {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
