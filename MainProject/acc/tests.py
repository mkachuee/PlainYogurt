from django.test import TestCase
from acc.forms import RegistrationForm
from acc.forms import LoginForm

# Create your tests here.
class AccTest(TestCase):
    def trivialTest(self):
        self.assertIs(True, True)

    def testRegistrationForm1(self):
        formData = {'username': 'qaz','password1': 'aaaaaaaaaa', 'password2': 'aaaaaaaaaa'}
        form = RegistrationForm(data=formData)
        self.assertTrue(form.is_valid())

    def testRegistrationForm2(self):
        formData = {'username': 'www','password1': 'aaaaaaaaaa', 'password2': 'bbbbbbbbbb'}
        form = RegistrationForm(data=formData)
        self.assertFalse(form.is_valid())

    def testRegistrationForm3(self):
        formData = {'username': 'too','password1': 'short', 'password2': 'short'}
        form = RegistrationForm(data=formData)
        self.assertFalse(form.is_valid())

    def testRegistrationForm4(self):
        formData = {'username': 'duplicate', 'password1': 'aaaaaaaaaa', 'password2': 'aaaaaaaaaa'}
        form = RegistrationForm(data=formData)
        form.save()
        self.assertTrue(form.is_valid())
        formData = {'username': 'duplicate', 'password1': 'aaaaaaaaaa', 'password2': 'aaaaaaaaaa'}
        form = RegistrationForm(data=formData)
        self.assertFalse(form.is_valid())

    def testRegistrationForm5(self):
        formData = {'username': 'sameUsernamePassword', 'password1': 'sameUsernamePassword', 'password2': 'sameUsernamePassword'}
        form = RegistrationForm(data=formData)
        self.assertFalse(form.is_valid())

    def testRegistrationForm6(self):
        formData = {'username': '!!!@@invalid', 'password1': 'aaaaaaaaaa', 'password2': 'aaaaaaaaaa'}
        form = RegistrationForm(data=formData)
        self.assertFalse(form.is_valid())

    def testRegistrationForm7(self):
        formData = {'username': '', 'password1': 'blank', 'password2': 'blank'}
        form = RegistrationForm(data=formData)
        self.assertFalse(form.is_valid())

    def testRegistrationForm8(self):
        formData = {'username': 'blank', 'password1': '', 'password2': ''}
        form = RegistrationForm(data=formData)
        self.assertFalse(form.is_valid())

    def testRegistrationForm9(self):
        formData = {'username': 'tooLong123456789012345678901234567890',
                    'password1': 'aaaaaaaaaa',
                    'password2': 'aaaaaaaaaa'}
        form = RegistrationForm(data=formData)
        self.assertFalse(form.is_valid())

    def testRegistrationForm10(self):
        formData = {'username': 'normal3',
                    'password1': 'tooLong123456789012345678901234567890',
                    'password2': 'tooLong123456789012345678901234567890'}
        form = RegistrationForm(data=formData)
        self.assertFalse(form.is_valid())

    def testRegistrationForm11(self):
        formData = {'username': 'tooLongB123456789012345678901234567890',
                    'password1': 'tooLongABCABCABCABCABCABCABCABCABCABCABCABC',
                    'password2': 'tooLongABCABCABCABCABCABCABCABCABCABCABCABC'}
        form = RegistrationForm(data=formData)
        self.assertFalse(form.is_valid())

    def testRegistrationForm12(self):
        for i in range(0,1000):
            formData = {'username': 'Spam'+str(i),
                        'password1': 'aaaaaaaaaa',
                        'password2': 'aaaaaaaaaa'}
            form = RegistrationForm(data=formData)
            self.assertTrue(form.is_valid())
            form.save()

    def testLoginForm1(self):
        formData = {'username': 'doesNotExist', 'password': 'aaaaaaaaaa'}
        form = LoginForm(data=formData)
        self.assertFalse(form.is_valid())

    def testLoginForm2(self):
        formData = {'username': 'working', 'password1': 'aaaaaaaaaa', 'password2': 'aaaaaaaaaa'}
        form = RegistrationForm(data=formData)
        form.save()
        formData = {'username': 'working', 'password': 'aaaaaaaaaa'}
        form = LoginForm(data=formData)
        self.assertTrue(form.is_valid())

    def testLoginForm3(self):
        formData = {'username': 'okay', 'password1': 'wrongPassword', 'password2': 'wrongPassword'}
        form = RegistrationForm(data=formData)
        form.save()
        formData = {'username': 'okay', 'password': 'wrong'}
        form = LoginForm(data=formData)
        self.assertFalse(form.is_valid())

    def testLoginForm3(self):
        formData = {'username': 'normal', 'password1': 'aaaaaaaaaa', 'password2': 'aaaaaaaaaa'}
        form = RegistrationForm(data=formData)
        form.save()
        formData = {'username': 'normal', 'password': ''}
        form = LoginForm(data=formData)
        self.assertFalse(form.is_valid())

    def testLoginForm4(self):
        formData = {'username': 'normal2', 'password1': 'aaaaaaaaaa', 'password2': 'aaaaaaaaaa'}
        form = RegistrationForm(data=formData)
        form.save()
        formData = {'username': '', 'password': 'aaaaaaaaaa'}
        form = LoginForm(data=formData)
        self.assertFalse(form.is_valid())
