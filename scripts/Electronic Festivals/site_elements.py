from bs4 import BeautifulSoup
from datetime import datetime

from fuzzywuzzy import process
from fuzzywuzzy import fuzz

from helper import *

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

def line_up(site, problem_djs, date):
    """
    Gets the line up from a given event. There are two possibilites where it appears on the site
    1. Current Line up -> Festival is yet to come and this is the Line Up (/event/her-damit)
    2. No Current Line up 
        2.1 Festival was in the past, then it is on former editions of the festival (/event/kult-festival)
        2.2 Festival is in the future and doesn't have line up yet (/event/no-mans-world)


    Arguments:
    site: site parsed with BS
    problem_djs: array to be filled with artist that have multiple matches
    date: date of event

    Return:
    artist_names: artists didn't match in Bookya DB
    arrist_urls: artists matched in Bookya DB

    Side Effects:
    Write Djs with multiple matches in Bookya DB to problem_djs array
    """

    state = site.find('h2').get_text()

    # 2. case in documentation
    if "No" in state:
        #now check date, we don't want to scrape a wrong line up that appears on site
        event_date = datetime.strptime(date, "%d/%m/%Y")
        lineup_date_ = site.find('div', {'class','field-date'}).get_text().strip()
        lineup_date = datetime.strptime(lineup_date_, "%B-%Y")
        #compare dates
        if event_date == lineup_date:
            line_up_block = site.find('div', {'class','field-lineup-tags'})
        else:
            return ' ', ' '
    # 1. case
    else:
        lineup_block = site.find('div', {'class','col-xs-12 nopadding list'})

    artist_names, artist_urls, problem_djs_ = extract_djs(lineup_block)
    problem_djs += problem_djs_
    return artist_names, artist_urls


def extract_djs(block):
    """
    The line_up method above decides, which line_up is valid. 
    This method extract the line up out of a given block handed over by 'line_up'

    Arguments: 
    block: html block with line up in it

    Return: 
    artist_names: artists didn't match in Bookya DB
    arrist_urls: artists matched in Bookya DB
    
    """

    artist_names = []
    artist_urls = []
    problem_djs = []

    for artist_ in block.find_all('a', href=True):
        artist = artist_.get_text()
        result_db = request_db(artist, 'artist')
        #artist is not in Bookya DB
        if not result_db['profiles']:
            artist_names.append(artist)
        #artist is in Bookya DB, one or multiple matches ? 
        elif len(result_db['profiles']) == 1:
            artist_urls.append(result['profiles'][0]['bookya_url'])
        else:
            found_dj = False
            #fuzzy matching rate
            factor = 0
            #iterate over results from db and see which artist has highest matching
            for index, artis in enumerate(result_db['profiles']):
                ratio = fuzz.ratio(dj, artis['name']) 
                if ratio >= 75 and ratio > factor:
                    factor = ratio
                    found_dj = True
                    artist_index = index

            #we found and artist with high matching probability
            if found_dj:
                artist_urls.append(result['profiles'][artist_index]['bookya_url'])
            #no artist found
            else:
                problem_djs.append(artist)

    return artist_names, artist_urls, problem_djs








