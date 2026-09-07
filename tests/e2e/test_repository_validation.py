import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.support import build_project


class RepositoryValidationE2ETests(unittest.TestCase):
    def test_deployable_project_passes_cli(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_project(root, "deployable")
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/validate_project_arch.py",
                    "--project-root",
                    str(root),
                    "--profile",
                    "deployable",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertIn("PASSED", result.stdout)


if __name__ == "__main__":
    unittest.main()
