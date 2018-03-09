from bs4 import BeautifulSoup
from datetime import datetime
import time

def genre(site):
    """
    Get genres of an event 

    Arguements:
    site: Site parsed with BS

    Return:
    genres: genres of an event
    """

    try:
        genre_list = []
        genres = site.find('div', {'class':'col-xs-12 col-sm-10 nopadding genrelist'})
        for genre in genres.find_all('a', href=True):
            buffer_str = genre.get_text()
            new_buffer = buffer_str.replace(" //", ",")
            genre_list.append(new_buffer)

        return ','.join(genre_list)
    except:
        return ''

def date(site):
    """
    Get Start date of a festival, depending on whether it's single or multi day

    Arguments:
    site: Site parsed with BS

    Return:
    start: start date
    """
    try:
        #get Date depending on whether its a Single or Multiday festival, also important for lineup
        duration = site.find('div', {'class': 'col-xs-auto col-sm-auto nopadding nomarginright disc'})
        #multi day festival
        if "Multi" in duration.get_text():
            start_multi_ = site.find('span', {'class':'date-display-start'})
            start_mutli = start_multi_.get_text()
            return start_mutli
        else:
            start_single_ = site.find('span', {'class':'date-display-single'})
            start_single = start_single.get_text()
            return start_single
    except:
        return ' '

def name(site):
    """
    Get name of an event 

    Arguements:
    site: Site parsed with BS

    Return:
    name: name of an event
    """
    try:
        festival_name = site.find('h1')
        name = festival_name.get_text()
        return name
    except: 
        return ' '

def bio(site):
    """
    Get bio of an event 

    Arguements:
    site: Site parsed with BS

    Return:
    bio: bio of an event
    """
    try:
        bio_ = site.find('div', {'class': 'col-xs-12 nopadding description'})
        bio = bio_.get_text().encode('utf-8')
        return bio
    except:
        return ' '

def homepage(site):
    """
    Get homepage of an event 

    Arguements:
    site: Site parsed with BS

    Return:
    homepage: homepage of event
    """

    try:
        homepage =  site.find('div', {'class': "col-xs-12 nopadding eventlinks link"})
        page_ = homepage.find('a', href=True)
        page = page_.get_text().encode('utf-8')
        return page
    except:
        return ' '

def location(site):
    """
    Get location of an event 

    Arguements:
    site: Site parsed with BS

    Return:
    location: location of an event
    """

    try:
        #get Location
        country_ = site.find('div', {'class': 'country-name'})
        country = country_.get_text().encode('utf-8')
        return country
    except:
        return ' '


def get_promo_urls(site):
    """
    Get Facebook and Youtube link from a given site

    site: Site parsed with BS

    Return:
    facebook: facebook link
    youtube: youtube link

    """
    try:
        facebook, youtube = '', '' 
        for urls in site.find_all('div', {'class': "col-xs-12 nopadding link"}):
            url = urls.find('a', href=True)
            link = url.get_text()
            if "facebook" in link:
                facebook = link
            if "youtube" in link:
                youtube = link

        return facebook, youtube
    except:
        return ' ', ' '







