from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_latest_entries(self):
        # Eelke has heard of the awesome new pipeline app.
        self.browser.get('http://localhost:8000')

        # Amased by the first impression, he looks to the tab title to make sure it's real
        self.assertIn('pipeline app - 4 real!', self.browser.title)

        # he sees the last entries scraped
        self.fail('Needs implementation')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
