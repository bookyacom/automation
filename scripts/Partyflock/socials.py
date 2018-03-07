from soup import get_soup
import re
from url_cleaner import *
import sys

def name(artist_page):
    """
    Simply return the name of an artist

    Argument:
    artist_page: page of an artist parsed with BS

    Return:
    name: name of the artist
    """

    try:
        name_ = artist_page.find('h2', {'itemprop': 'name'})
        name = name_.getText()
        return name
    except:
        print("Unexpected error in name function", sys.exc_info()[0])
        return ' '

def get_socials(artist_page, ws, row):
    """
    Get all the social media data from Partyflock for given artist

    Arguments:
    artist_page: page of artist parsed with BS
    ws: Workbook
    row: index of current row

    Side effects:
    Write into Workbook (Excel File)

    Return: None
    """
    try: 
        presence_row = artist_page.find('tr', {'class': 'presencerow'})
        social_links = presence_row.find_all('a', title=True)
        for link in social_links:
            social_info = link['title']
            #check what kind of link it is and clean it from www, https:// etc.
            if 'facebook' in social_info:
                ws.cell(row=row, column = 4).value = facebook(social_info)
            elif 'soundcloud' in social_info:
                ws.cell(row=row, column = 11).value = soundcloud(social_info)
            elif 'twitter' in social_info:
                ws.cell(row=row, column = 13).value = twitter(social_info)
            elif 'youtube' in social_info:
                ws.cell(row=row, column = 14).value = youtube(social_info)
            elif 'instagram' in social_info:
                ws.cell(row=row, column = 6).value = instagram(social_info)
            elif 'spotify' in social_info:
                ws.cell(row=row, column = 12).value = spotify(social_info)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        pass

def website(artist_page):
    """
    Get the website of a given artist on Partyflock

    Arguments:
    artist_page: page of artist parsed with BS

    Return: 
    site: website of artist
    """
    try: 
        table = artist_page.find('table', {'class':'nodyn deflist vtop'})
        site = table.find('img', {'alt': 'Site'})
        site = site['title']
        return site
    except:
        return ' '

def genres(artist_page):
    """
    Get the genres of a given artist page

    Arguments:
    artist_page: page of artist parsed with BS
    
    Return:
    genres: list of genres

    """
    try:
        genres = []
        table = artist_page.find('table', {'class':'nodyn deflist vtop'})
        for block in table.find_all('a', href=True):
            if "/party/" in block['href']:
                genres.append(block.getText())

        return ','.join(genres)
    except:
        print("Unexpected error in genres function", sys.exc_info()[0])
        return ' '

def email(artist_page):
    """
    Get the email of a given artist page

    Arguments:
    artist_page: page of artist parsed with BS
    
    Return:
    

    """
    try:
        table = artist_page.find('table', {'class':'nodyn deflist vtop'})
        for block in table.find_all('a', href=True):
            if re.search('mailto', block['href']):
                mail = block.getText()
                return mail
        return ' '
    except:
        print("Unexpected error in email function", sys.exc_info()[0])
        return ' '

def bio(artist_page):
    """
    Get the Bio of a given artist page on Partyflock
    
    Arguments:
    artist_page: page of artist parsed with BS

    Return: 
    bio: biography of artist


    """
    try: 
        bio_ = artist_page.find('div', {'id': 'biobody'} )
        bio = bio_.getText()
        return bio
    except: 
        try:
            bio_ = artist_page.find('article', {'data-partyflock-type': 'bio'})
            bio_ = bio_.getText()
            #Regex to delete everything up to a year date 
            # --> Beginning of Biographie is "Biographie 23. may 2018"
            bio = re.sub(r'.+\d{4}', '', bio_)
            return bio.strip()
        except:
            print("Unexpected error in bio function", sys.exc_info()[0])
            return ' '

def labels(artist):
    """
    Get all recordlabels for a given artist from labelsbase.net
    """
    labelbase_url = 'https://labelsbase.net/search?a='

    artist_query = re.sub('[&]', '%26', artist)
    artist_query = re.sub('[ ]', '+', artist_query)
    url = labelbase_url + artist_query
    soup = get_soup(url)
    labels = []
    try:
        for label_div in soup.find_all('div', {'class': 'col-sm-6 col-xs-12 label-item'}):
            label_info = label_div.find_all('a', href=True)
            labels.append(label_info[1].getText())

        return ','.join(labels)

    except:
        print("Unexpected error in labels function", sys.exc_info()[0])
        return ' '