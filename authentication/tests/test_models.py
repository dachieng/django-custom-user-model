from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_creates_user(self):
        # check if the user can be created
        user = User.objects.create_user(
            "dorcas", "oloodorcas99@gmail.com", "teddy@123")

        # check if the created user is an instance of user
        self.assertIsInstance(user, User)

        # check if the user.email equals the email given
        self.assertEqual(user.email, 'oloodorcas99@gmail.com')

        # check if is_staff is det to false
        self.assertFalse(user.is_staff)

    def test_creates_superuser(self):
        user = User.objects.create_superuser(
            'camille', 'camille@gmail.com', 'teddy@123')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'camille@gmail.com')

        # is_staff must be set to true
        self.assertTrue(user.is_staff)

    def test_raise_valueerror_for_username_not_provided(self):
        self.assertRaises(ValueError, User.objects.create_user, username='',
                          email='oloodorcas99@gmail.com', password='teddy@123')

        # optional
        self.assertRaisesMessage(ValueError, 'The given username must be set')

    def test_raise_value_error_email_not_provided(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username="dorcas", email="", password="teddy@123")
        self.assertRaisesMessage(ValueError, 'The given email must be set')

    def test_is_staff(self):
        self.assertRaises(ValueError, User.objects.create_superuser,
                          username="dorcas", email="oloodorcas99@gmail.com", password="teddy@123", is_staff=False)

    def test_check_is_super_user(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username="oloo",
                          email='oloodorcas99@gmail.com', password="teddy@123", is_superuser=False)
