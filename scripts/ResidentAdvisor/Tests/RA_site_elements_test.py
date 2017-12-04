import sys
sys.path.append('../')

import unittest
from RA_site_elements import *
from soup import get_soup_js, get_soup
from bs4 import BeautifulSoup

global soup, url, top_bar, sites
url = 'https://www.residentadvisor.net/club.aspx?id=90016'
soup = get_soup_js(url)
top_bar = soup.find('ul', {'class': 'clearfix'})
sites = top_bar.find_all('a', href= True)

class Tests(unittest.TestCase):

    def test_soup(self):
        a_tags = soup.find_all('a', href=True)
        self.assertEqual(125, len(a_tags))

    def test_bio(self):
        bio_test = 'Restaurant + Bar turns into nightclub on weekends'.encode('utf-8')
        bio_ = bio(soup)
        self.assertEqual(bio_test, bio_)

    def test_address(self):
        address_test = 'Oskar Laredo Platz 1, 97080 Würzburg  Germany'.encode('utf-8')
        address_ = address(soup)
        self.assertEqual(address_, address_test)

    def test_picture(self):
        pic_link = 'https://www.residentadvisor.net/images/clubs/de-ms-z.jpg'
        pic = picture(soup)
        self.assertEqual(pic, pic_link)

    def test_homepage(self):
        site_test = ('http://neueliebealterhafen.de', ' ')
        site_ = homepage(sites)
        self.assertEqual(site_test, site_)

    def test_email(self):
        email_test = 'info@neueliebealterhafen.de'
        email_ = mail(sites)
        self.assertEqual(email_test, email_)

    def test_capacity(self):
        capacity_test = '175'
        capacity_ = capacity(top_bar)
        self.assertEqual(capacity_test, capacity_)

    def test_phone(self):
        phone_ = phone(top_bar)
        self.assertEqual(phone_, ' ')

    def test_get_events(self):
        events = []
        get_events(soup, events)
        self.assertTrue(events)


if __name__ == '__main__':
    unittest.main()
