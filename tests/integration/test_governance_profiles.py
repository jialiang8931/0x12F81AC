import tempfile
import unittest
from pathlib import Path

from scripts.validate_project_arch import validate_project
from tests.support import build_project


class GovernanceProfileTests(unittest.TestCase):
    def test_docs_only_profile_passes_minimal_layout(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_project(root, "docs-only")
            self.assertTrue(validate_project(root, "docs-only").passed)

    def test_service_requires_docker_and_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_project(root, "docs-only")
            errors = validate_project(root, "service").errors
            self.assertTrue(any("infra/docker/Dockerfile" in error for error in errors))
            self.assertTrue(any("scripts/manifest.json" in error for error in errors))

    def test_service_manifest_requires_full_delivery_lifecycle(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_project(root, "service")
            (root / "scripts/manifest.json").write_text(
                '{"delivery_lifecycle": ["test", "e2e"], "public_entrypoints": []}\n',
                encoding="utf-8",
            )
            errors = validate_project(root, "service").errors
            self.assertTrue(any("delivery lifecycle" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
