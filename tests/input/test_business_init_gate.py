import tempfile
import unittest
from pathlib import Path

from scripts.validate_project_arch import validate_business_init
from tests.support import INIT_TEXT


class BusinessInitGateTests(unittest.TestCase):
    def test_accepts_user_ready_bdd_document(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "init.md"
            path.write_text(INIT_TEXT, encoding="utf-8")
            self.assertEqual((), validate_business_init(path))

    def test_rejects_ai_owner_and_placeholder(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "init.md"
            path.write_text(
                INIT_TEXT.replace("domain-team", "AI").replace("無。", "TODO"),
                encoding="utf-8",
            )
            errors = validate_business_init(path)
            self.assertTrue(any("business_owner" in error for error in errors))
            self.assertTrue(any("placeholder" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
