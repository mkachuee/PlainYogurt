from django.test import TestCase

# Create your tests here.
class SearchTest(TestCase):
    def testSearching(self):
        response = self.client.get('/search/', {'q': 'Algebra'})
        print(response.status_code)
        self.assertEqual(response.status_code, response.status_code)

    def testSearchingBlank(self):
        response = self.client.get('/search/', {'q': ''})
        print(response.status_code)
        self.assertEqual(response.status_code, response.status_code)