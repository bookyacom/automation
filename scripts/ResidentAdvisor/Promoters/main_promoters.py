import sys 
import os 
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))+ '/..'))

from venue_ids import get_ids
from RA_country import scrape_country

file_path = '/Users/nequalstim/Desktop/bookya/temp'

if len(sys.argv) < 2: 
    print('USAGE: [country name] ([File.txt])')
    sys.exit()

#take country names via cmd line
countries = sys.argv

country = countries[1]

#links of country will be collected and scraped
if len(countries) == 2:

    country_overview = get_ids(country)
    for country, ids in country_overview.items():

        RA_Id = ids['ra_id']
        end = ids['end']

        links = []

        # get all the venue links from all of COUNTRY and save them to links
        for x, y in zip(ra_id, end):
            get_all_links(x, y, links, "promoter")

        scrape_links_promoter(links, country)


#user gave file with links, which will be scraped
if len(countries) == 3:

    file_name = countries[2]
    filtered_links = [line.rstrip('\n') for line in open(os.path.join(file_path, file_name), 'r')]



