import requests
from soup import get_soup, get_soup_js

def get_all_links (RA_id, list_end, links, club_promoter):
    """
    get links from all the venues/promoters on a given site

    Arguments:
    RA_id: Id from city/country
    list_end:  ID of last club/promoter on the list (break point)
    club: boolean, club or promoter?
          1: club 0: promoter

    Side effect:
    links: gets filled with RA club/promoter links
    """
    if (club_promoter):
        url = "https://www.residentadvisor.net/clubs.aspx?ai=" + str(RA_id)
        criteria = 'club.aspx?'
    else:
        url = "https://www.residentadvisor.net/promoters.aspx?ai=" + str(RA_id)
        criteria = 'promoter.aspx?'

    soup = get_soup(url)

    for a in soup.find_all('a', href=True):
        if criteria in a['href']:
            links.append("https://www.residentadvisor.net" + a['href'])
        #marking the end of the list
        if str(list_end) in a['href']:
        	break

def filter_links(links):
    """
    iterate over venue/promoter links and clean out the ones which didn't have a
    listing in 2016 (criteria for venue/promoter not active)

    Arguments:
    links: Array of venue/promoter links

    Return:
    links_filtered: Filtered list

    """

    links_dirty = []
    for link in links:
        soup = get_soup_js(link)
        #archive
        try:
            archive_listing = soup.find('div', {'id': 'divArchiveEvents'})
            events = archive_listing.find_all('ul', {'class': 'ptb8'})
            for event in events:
                time_ = event.find('li', {'style': 'height: auto;'})
                time = time_.get_text()
                if '2016' in time:
                    links_dirty.append(link)
                    break
                elif '2017' in time:
                    links_dirty.append(link)
                    break
        except:
            pass

    # clean out duplicates
    links_filtered = sorted(list(set(links_dirty)))

    return links_filtered
