"""
Start point of the scraper, where user gives the names of the countries he would like 
to have scraped as a command line argument. 

The corresponding IDs of each country are stored in a dictionary and subsequently scraped for 
their venue links. These venue_links are handed over to the next method then -> scrape_links_venue
"""

import sys 
import os 
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))+ '/..'))

from venue_ids import get_ids
from RA_links import get_all_links
from scrape_links import scrape_links_venue

file_path = os.getcwd()

if len(sys.argv) < 2: 
    print('USAGE: python3 main_venues.py [countries]')
    sys.exit()

#take country names via cmd line
countries = sys.argv[1:]
print(countries)

#links of country will be collected and scraped
country_ids = get_ids(countries)
for country, ids in country_ids.items():

    RA_Id = ids['ra_id']
    end = ids['end']

    venue_links = []

    # get all the venue links from all of COUNTRY and save them to links array
    for x, y in zip(RA_Id, end):
        """ extract all the links of venues for a given country
            some countries just have on site on RA (Cuba)
            some are divided into multiple (Germany -> Bavaria, Berlin etc.) """
        get_all_links(x, y, venue_links, "venue")

    #scrape the collected links 
    scrape_links_venue(venue_links, country)
