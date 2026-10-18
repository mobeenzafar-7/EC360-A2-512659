import unittest

from auth_service import register_user


class TestRegistration(unittest.TestCase):
    def test_successful_registration(self):
        user = register_user("alice@example.com", "a-strong-password-12")
        self.assertEqual(user["email"], "alice@example.com")
        self.assertEqual(user["status"], "pending_verification")

    def test_short_password_rejected(self):
        with self.assertRaises(ValueError):
            register_user("alice@example.com", "short")


if __name__ == "__main__":
    unittest.main()