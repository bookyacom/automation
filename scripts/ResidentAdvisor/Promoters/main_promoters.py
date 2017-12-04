import sys
sys.path.append('../')

from promoter_ids import get_ids
from RA_country import scrape_country

country_overview = get_ids('Argentina')

for country, ids in country_overview.items():

    RA_Id = ids['ra_id']
    end = ids['end']

    scrape_country(country, RA_Id, end, False)
