import sys
sys.path.append('../')

import unittest
from RA_links import *

class Tests(unittest.TestCase):

    def test_get_all_links(self):
        url = 'https://www.residentadvisor.net/clubs.aspx?ai=154'
        links = []
        get_all_links(154, 132967, links, True)
        self.assertEqual(49, len(links))

    def test_filter_clubs(self):
        venue_links = [
            'https://www.residentadvisor.net/club.aspx?id=90016',
            'https://www.residentadvisor.net/club.aspx?id=111711',
            'https://www.residentadvisor.net/club.aspx?id=34536'
        ]

        filtered = filter_link(venue_links)
        filter_

        self.assertEqual(2, len(filtered))

if __name__ == '__main__':
    unittest.main()
