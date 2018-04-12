from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_see_latest_entries(self):
        # Eelke has heard of the awesome new pipeline app.
        self.browser.get('http://localhost:8000')

        # Amased by the first impression, he looks to the tab title to make sure it's real
        self.assertIn('pipeline - 4 real!', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Scraped', header_text)

        # Eelke sees he can edit some data himself
        inputbox = self.browser.find_element_by_id('edit_data')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Modify data')

        # Eelke really likes Sam Feldt, he knows Sam is a fellow dutchie
        # but the scraper say he is german, that's (very) wrong! he needs to edit the
        # data straigth away!
        inputbox.send_keys('NL')

        # When he press enter, the site updates, and the data is changed
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id("artist_table")
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('NL', [row.text for row in rows],
                        'New info did not appear in the table -- its text was:\n%s' % (
                            table.text,
                        ))

        # Eelke sees more mistake in the data, but he is going for lunch first
        self.fail('Needs implementation')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
