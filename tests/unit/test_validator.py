import unittest

from scripts.validate_project_arch import parse_front_matter, required_paths


class ValidatorUnitTests(unittest.TestCase):
    def test_parses_simple_front_matter(self) -> None:
        text = "---\nbusiness_owner: team\nstatus: READY_FOR_GOVERNANCE\n---\n# Body\n"
        self.assertEqual(
            {"business_owner": "team", "status": "READY_FOR_GOVERNANCE"},
            parse_front_matter(text),
        )

    def test_deployable_extends_service(self) -> None:
        service = set(required_paths("service"))
        deployable = set(required_paths("deployable"))
        self.assertLess(service, deployable)
        self.assertIn("infra/terraform", deployable)


if __name__ == "__main__":
    unittest.main()
