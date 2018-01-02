from RA_links import get_all_links, filter_links
from scrape_links import scrape_links_venue, scrape_links_promoter
from RA_site_elements import write_to_file
import os

def scrape_country(country, club_promoter):
    """
    Arguments:
    country: name of country to be scraped
    ra_id: resident advisor id of country
    end: id of the last club in the list (stop criteria)
    club_promoter: boolean, club or promoter?
        1: club 0: promoter

    Return:
    None

    Side Effects:
    Creates excel file named country.xlsx with all the clubs filtered and scraped
    Creates txt file names country_venues.txt with a list of a countries clubs
    """

    # filter out all the venues that didn't have an event in 2016,2017
    filtered_links = filter_links(links)
    file_path = '/Users/nequalstim/Desktop/bookya/temp'
    file_name = 'USA_venues_test.txt'

    if (club_promoter):
        link_file = open(os.path.join(file_path, country+'_venues.txt'), 'w')
    else:
        link_file = open(os.path.join(file_path, country+'_promoters.txt'), 'w')


    write_to_file(filtered_links, link_file)

    #just in case, we have to run it again to extract data, we don't have to filter all the links from scratch
    filtered_links = [line.rstrip('\n') for line in open(os.path.join(file_path, file_name), 'r')]
    #extract all the data from the venue pages and write it to excel file
    #additionally write the event links of each club to seperate file
    if(club_promoter):
        scrape_links_venue(filtered_links, country)
    else:
        scrape_links_promoter(filtered_links, country)
