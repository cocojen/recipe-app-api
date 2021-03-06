from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@google.com'
        password = 'Testpass1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        # password 는 암호화되기 때문에 check_password() 를 사용해야함
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@GOOGLE.COM'
        user = get_user_model().objects.create_user(email, 'Testpass1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@google.com')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@google.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
