import os
from soup import get_soup, get_soup_js
from openpyxl import Workbook
from RA_site_elements import *
from bs4 import BeautifulSoup


def scrape_links_venue(links, country):

    """
    The brain of the scraper. Takes in link and calls all individual scraper functions.

    Arguments:
    links: array of residentadvisor links
    country: Name of country to be scraped

    Return:
    None

    Side Effects:
    Create Excel File and fill it with all the scraped information
    """
    wb = Workbook()
    filename1 = country + '_venues.xlsx'
    ws = wb.active
    ws.title = country

    set_up_club(ws)

    file_path = '/Users/nequalstim/Desktop/bookya/temp'

    events=[]
    for y, item in enumerate(links, start=1):
        soup = get_soup_js(item)

        ws.cell(row = y, column = 1).value = item

        # print out sorted (nach residentadvisorlink) list of clubs
        clubname = soup.find('h1').string.encode('utf-8')
        ws.cell(row = y, column = 2).value = clubname

        #get picture links
        ws.cell(row = y, column = 3).value = picture(soup)

        # print bio to file
        ws.cell(row = y, column = 8).value = bio(soup)

        #print adresses of clubs
        ws.cell(row = y, column = 14).value = address(soup)


        top_bar = soup.find('ul', {'class': 'clearfix'})
        sites = top_bar.find_all('a', href= True)

        #Get Website and Facebook
        website, facebook_page = homepage(sites)
        ws.cell(row = y, column = 9).value = website
        ws.cell(row = y, column = 20).value = facebook_page

        #get email
        ws.cell(row = y, column = 5).value = mail(sites)

        #Get capacity number
        ws.cell(row = y, column = 13).value = capacity(top_bar)

        #Get contact number
        ws.cell(row=y, column = 7).value = phone(top_bar)

        #extract all the event links from venues
        # put a space in empty cells for nicer formatting in excel
        get_events(soup, events)

        placeholders(ws,y)

    events_file = open(os.path.join(file_path, country+'_event.txt'), 'w')
    write_to_file(events, events_file)
    wb.save(file_path + '/' + filename1)

def scrape_links_promoter(links, country):

    """
    The brain of the scraper. Takes in link and calls all individual scraper functions.


    Arguments:
    links: array of residentadvisor links
    country: Name of country to be scraped

    Return:
    None

    Side Effects:
    Create Excel File and fill it with all the scraped information
    """
    wb = Workbook()
    filename1 = country + '_promoters.xlsx'
    ws = wb.active
    ws.title = country

    set_up_promoter(ws)

    file_path = '/Users/nequalstim/Desktop/bookya/temp'

    events=[]
    for y, item in enumerate(links, start=1):
        soup = get_soup_js(item)

        #RA_link
        ws.cell(row = y, column = 3).value = item


        promoter_name = soup.find('h1').string.encode('utf-8')
        ws.cell(row = y, column = 1).value = promoter_name

        #get picture links
        ws.cell(row = y, column = 7).value = picture(soup)

        # print bio to file
        ws.cell(row = y, column = 8).value = bio(soup)

        top_bar = soup.find('ul', {'class': 'clearfix'})
        sites = top_bar.find_all('a', href= True)

        #Get Website and Facebook
        website, facebook_page = homepage(sites)
        ws.cell(row = y, column = 5).value = website
        ws.cell(row = y, column = 6).value = facebook_page

        #get email
        ws.cell(row = y, column = 10).value = mail(sites)

        placeholders = [2, 4, 9]
        for column in placeholders:
            ws.cell(row = y, column = column).value = " "
        #extract all the event links from venues
        # put a space in empty cells for nicer formatting in excel
        get_events(soup, events)
        events_filtered = list(set(events))

    events_file = open(os.path.join(file_path, country+'_event.txt'), 'w')
    write_to_file(events_filtered, events_file)
    wb.save(file_path + '/' + filename1)

def scrape_links_event(links):
    wb = Workbook()
    filename1 = 'RA_events.xlsx'
    ws = wb.active

    set_up_event(ws)

    file_path = '/Users/nequalstim/Desktop/bookya/temp'

    problem_artists = []

    for y, link in enumerate(links, start=1):
        soup = get_soup(link)

        ws.cell(row=y, column=1).value = name(soup)

        ws.cell(row=y, column = 4).value = "noreply@bookya.com"

        div_event_item = soup.find("div", {"id": "event-item"})
        p_tags = div_event_item.find_all('p')

        #get line up
        notBookya, bookya, problem_artists = line_up(p_tags, problem_artists)
        ws.cell(row=y, column = 22).value = ','.join(notBookya)
        ws.cell(row=y, column = 23).value = ','.join(bookya)

        #get bio
        ws.cell(row=y, column=10).value = bio_event(p_tags)

        #get flyer picture
        ws.cell(row=y, column=3).value = flyer_picture(div_event_item)

        #dates and venue both need a_tags from top_bar
        top_bar = soup.find('ul', {'class': 'clearfix'})
        a_tags = top_bar.find_all('a', href=True)

        start_date, end_date = dates(a_tags)
        ws.cell(row=y, column=13).value = start_date
        ws.cell(row=y, column=14).value = end_date

        found_venue, venue_name = venue(a_tags)
        if (found_venue):
            ws.cell(row=y, column=21).value = venue_name
        else:
            ws.cell(row=y, column=20).value = venue_name

        #get costs for event
        li = top_bar.find_all('li')
        cost, currency = costs(li)
        ws.cell(row=y, column = 15).value = cost
        ws.cell(row=y, column = 16).value = currency

        found_prom, promoter_name = promoter(li)
        if(found_prom):
            ws.cell(row=y, column=19).value = promoter_name
        else:
            ws.cell(row=y, column=18).value = promoter_name

        # put a space in empty cells for nicer formatting in excel
        placeholders = [2, 5, 6, 7, 8, 9, 11, 12, 17, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        for column in placeholders:
            ws.cell(row = y, column = column).value = " "

    artistfile = open(os.path.join(file_path, 'problem_artists.txt'), 'w')
    problem_artists = list(set(problem_artists))
    write_to_file(problem_artists, artistfile)
    wb.save(file_path + '/' + filename1)

def set_up_club (ws):
    """
    Initialize the Excel File with the Header

    Arguments:
    ws: active Workbook

    Return:
    None
    """
    ws.cell(row=1, column = 1).value = "RA_URL"
    ws.cell(row=1, column = 2).value = "dispay_name"
    ws.cell(row=1, column = 3).value = "profile_photo"
    ws.cell(row=1, column = 4).value = "email"
    ws.cell(row=1, column = 5).value = "public_email"
    ws.cell(row=1, column = 6).value = "public_contact_number"
    ws.cell(row=1, column = 7).value = "contact_number"
    ws.cell(row=1, column = 8).value = "bio"
    ws.cell(row=1, column = 9).value = "websites"
    ws.cell(row=1, column = 10).value = "genre_list"
    ws.cell(row=1, column = 11).value = "type_list"
    ws.cell(row=1, column = 12).value = "performance_area_count"
    ws.cell(row=1, column = 13).value = "capacity"
    ws.cell(row=1, column = 14).value = "address_line_one"
    ws.cell(row=1, column = 15).value = "address_line_two"
    ws.cell(row=1, column = 16).value = "external_id"
    ws.cell(row=1, column = 17).value = "city"
    ws.cell(row=1, column = 18).value = "country"
    ws.cell(row=1, column = 19).value = "contact_person"
    ws.cell(row=1, column = 20).value = "facebook_page"
    ws.cell(row=1, column = 21).value = "instagram"
    ws.cell(row=1, column = 22).value = "mixcloud"
    ws.cell(row=1, column = 23).value = "patryflock"
    ws.cell(row=1, column = 24).value = "songkick"
    ws.cell(row=1, column = 25).value = "twitter"
    ws.cell(row=1, column = 26).value = "youtube_channel"

def set_up_promoter (ws):
    """
    Initialize the Excel File with the Header

    Arguments:
    ws: active Workbook

    Return:
    None
    """
    #initialitze table with values
    ws.cell(row=1, column = 1).value = "Name Promoter"
    ws.cell(row=1, column = 2).value = "Location"
    ws.cell(row=1, column = 3).value = "RA_link"
    ws.cell(row=1, column = 4).value = "Genre"
    ws.cell(row=1, column = 5).value = "Website"
    ws.cell(row=1, column = 6).value = "Facebook"
    ws.cell(row=1, column = 7).value = "Picture"
    ws.cell(row=1, column = 8).value = "Bio"
    ws.cell(row=1, column = 9).value = "Contact Person"
    ws.cell(row=1, column = 10).value = "Email"

def set_up_event (ws):

	"""
    Initialize the Excel File with the Header

    Arguments:
	ws: active Workbook

    Return:
	None
    """

	ws.cell(row=1, column = 1).value = "display_name"
	ws.cell(row=1, column = 2).value = "profile_photo"
	ws.cell(row=1, column = 3).value = "cover_photo"
	ws.cell(row=1, column = 4).value = "email"
	ws.cell(row=1, column = 5).value = "public_email"
	ws.cell(row=1, column = 6).value = "public_contact_number"
	ws.cell(row=1, column = 7).value = "search_artist"
	ws.cell(row=1, column = 8).value = "header_text"
	ws.cell(row=1, column = 9).value = "contact_number"
	ws.cell(row=1, column = 10).value = "bio"
	ws.cell(row=1, column = 11).value = "websites"
	ws.cell(row=1, column = 12).value = "genre_list"
	ws.cell(row=1, column = 13).value = "start_date"
	ws.cell(row=1, column = 14).value = "end_date"
	ws.cell(row=1, column = 15).value = "ticket_price"
	ws.cell(row=1, column = 16).value = "ticket_currency"
	ws.cell(row=1, column = 17).value = "contact_person"
	ws.cell(row=1, column = 18).value = "promoter_name"
	ws.cell(row=1, column = 19).value = "promoter_url"
	ws.cell(row=1, column = 20).value = "venue_name"
	ws.cell(row=1, column = 21).value = "venue_url"
	ws.cell(row=1, column = 22).value = "artist_names"
	ws.cell(row=1, column = 23).value = "artist_urls"
	ws.cell(row=1, column = 24).value = "facebook_page"
	ws.cell(row=1, column = 25).value = "beatport_dj"
	ws.cell(row=1, column = 26).value = "instagram"
	ws.cell(row=1, column = 27).value = "lastfm"
	ws.cell(row=1, column = 28).value = "mixcloud"
	ws.cell(row=1, column = 29).value = "partyflock"
	ws.cell(row=1, column = 30).value = "songkick"
	ws.cell(row=1, column = 31).value = "soundcloud"
	ws.cell(row=1, column = 32).value = "spotify"
	ws.cell(row=1, column = 33).value = "twitter"
	ws.cell(row=1, column = 34).value = "youtube_channel"
	ws.cell(row=1, column = 35).value = "bandsintown"
