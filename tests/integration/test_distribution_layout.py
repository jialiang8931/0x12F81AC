import unittest
from pathlib import Path

from scripts.validate_project_arch import parse_front_matter


class DistributionLayoutTests(unittest.TestCase):
    def test_repository_root_is_installable_skill(self) -> None:
        root = Path(__file__).resolve().parents[2]
        metadata = parse_front_matter((root / "SKILL.md").read_text(encoding="utf-8"))
        self.assertEqual("project-arch-init", metadata.get("name"))
        self.assertTrue((root / "agents/openai.yaml").is_file())
        self.assertTrue((root / "references/business-init-gate.md").is_file())

    def test_readme_documents_root_install_route(self) -> None:
        root = Path(__file__).resolve().parents[2]
        readme = (root / "README.md").read_text(encoding="utf-8")
        self.assertIn("jialiang8931/0x12F81AC", readme)
        self.assertIn("--path . --name project-arch-init --ref main", readme)


if __name__ == "__main__":
    unittest.main()
