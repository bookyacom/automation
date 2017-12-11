import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))+ '/..'))
from RA_country import scrape_country

from promoter_ids import get_ids

if len(sys.argv) < 2: 
	print('Give me the name of at least one country')
	sys.exit()

#take country names from command line 
countries = sys.argv

country_overview = get_ids(countries[1:])

for country, ids in country_overview.items():

    RA_Id = ids['ra_id']
    end = ids['end']

    scrape_country(country, RA_Id, end, False)
