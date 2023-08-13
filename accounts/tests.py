from django.test import TestCase
from accounts.forms import CustomUserCreationForm

# Unit Test Cases for user create 

class CustomerUserCreationTestCase(TestCase):
    def test_valid_form(self):
        data = {
            'username': 'joebloggs',
            'email': 'testcase@bu.edu',
            'first_name': 'Joe',
            'last_name': 'Bloggs',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = CustomUserCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'username': 'joebloggs',
            'email': 'testcase@bu.edu',
            'first_name': 'This is a test case to see if the max length of 30 characters works for this particular accounts form',  
            'last_name': 'Bloggs',
            'password1': 'testpassword',
            'password2': 'testpassword'

        }
        form = CustomUserCreationForm(data=data)
        self.assertFalse(form.is_valid())
