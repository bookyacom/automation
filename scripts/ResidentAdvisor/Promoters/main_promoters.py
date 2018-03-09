"""
Start point of the scraper, where user gives the names of the countries he would like 
to have scraped as a command line argument. 

The corresponding IDs of each country are stored in a dictionary and subsequently scraped for 
their promoter links. These promoter_links are handed over to the next method then -> scrape_links_promoter
"""

import sys 
import os 
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))+ '/..'))

from venue_ids import get_ids

file_path = os.getcwd()

if len(sys.argv) < 2: 
    print('Give the name of at least one country')
    print('USAGE: python3 main_promoters.py [countries]')
    sys.exit()

#take country names via cmd line
countries = sys.argv[1:]

country_overview = get_ids(country)
for country, ids in country_overview.items():

    RA_Id = ids['ra_id']
    end = ids['end']

    promoter_links = []

    # get all the promoter links from a country and save them to promoter_links
    for x, y in zip(ra_id, end):
        get_all_links(x, y, promoter_links, "promoter")

    #scrape the collected links
    scrape_links_promoter(promoter_links, country)




