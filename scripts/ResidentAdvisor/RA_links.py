import requests
from soup import get_soup, get_soup_js
from bs4 import BeautifulSoup

def get_all_links (RA_id, list_end, links, switch):
    """
    Get links from all the venues/promoters on a given site

    Arguments:
    RA_id: Id from city/country
    list_end:  ID of last club/promoter on the list (break point)
    switch: determines whether it's a venue or promoter

    Side effect:
    links: gets filled with RA club/promoter links
    """
    if switch == "venue":
        url = "https://www.residentadvisor.net/clubs.aspx?ai=" + str(RA_id)
        criteria = 'club.aspx?'
    elif switch == "promoter":
        url = "https://www.residentadvisor.net/promoters.aspx?ai=" + str(RA_id)
        criteria = 'promoter.aspx?'

    soup = get_soup(url)

    for a in soup.find_all('a', href=True):
        if criteria in a['href']:
            links.append("https://www.residentadvisor.net" + a['href'])
        #marking the end of the list
        if str(list_end) in a['href']:
            break

def active(soup):
    """
    check whether a given listing is still active or not
    criteria: Did the club host an event in 2016/2017/2018?

    Arguments:
    soup: page of venue/promoter parsed with BS

    Return:
    True: club had an event in 2016/2017/2018
    False: club is not active anymore

    """

    #archive of events 
    try:
        archive_listing = soup.find('div', {'id': 'divArchiveEvents'})
        events = archive_listing.find_all('ul', {'class': 'ptb8'})
        for event in events:
            time_ = event.find('li', {'style': 'height: auto;'})
            time = time_.get_text()
            if '2016' in time:
                return True
            elif '2017' in time:
                return True
            elif '2018' in time:
                return True

        return False
    except:
        return Fals