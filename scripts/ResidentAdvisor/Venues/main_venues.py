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

    links = []

    # get all the venue links from all of COUNTRY and save them to links
    for x, y in zip(RA_Id, end):
        #extract all the links of venues for a given country
        get_all_links(x, y, links, "venue")

    #scrape the collected links 
    scrape_links_venue(links, country)




