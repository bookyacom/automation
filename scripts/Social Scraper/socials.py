import re
from soup import get_soup, get_soup_js

#URLS
lastfm_url = 'https://www.last.fm/de/search?q='
sk_url = 'http://www.songkick.com/search?utf8=%E2%9C%93&type=initial&query='
google_url = "https://www.google.de/search?q="
partyflock_url = 'https://partyflock.nl/artist/searchresult?NAME='
labelbase_url = 'https://labelsbase.net/?a='



def artist_to_query(artist):
    """
    brings artist name into right format for google/lastfm/songkick queries

    Arguments:
    artist: artist name

    Return:
    artist_query: artist name in right format

    Example
    Ben Klock --> Ben+Klock
    Tiger & Woods --> Tiger+Woods
    """

    artist_query = re.sub('[&]', '%26', artist)
    artist_qurey = re.sub('[ ]', '+', artist_query)
    return artist_query

def lastfm(artist):
    """
    Get lastfm ID for given artist straight from lastfm website 

    Arguments:
    artist: name of artist

    Return: 
    link_clean: lastfm id

    Example:
    lastfm(Ben Klock) -> music/Ben+Klock
    """
    artist_lf = artist_to_query(artist)
    artist_lf = artist_lf.replace("´","")
    url = lastfm_url + artist_lf
    soup = get_soup(url)
    lastfm = soup.find("div", {"class": "grid-items-item-details"})
    try:
        link_dirty = lastfm.find("a")
        link_clean = link_dirty['href'].replace("/de/","")
        return link_clean
    except:
        return ' '

def songkick(artist):
    """
    Get songkick ID for given artist straight from songkick website 

    Arguments:
    artist: name of artist

    Return: 
    link_clean: songkick id

    Example:
    songkick(Ben Klock) -> 286113-ben-klock
    """
    artist_sk = artist_to_query(artist)
    artist_sk = artist_sk.replace("´","")
    url = sk_url + artist_sk
    soup = get_soup(url)
    songkick = soup.find("li", {"class": "artist"})
    try:
        link_dirty = songkick.find("a")
        link_clean = link_dirty['href'].replace("/artists/","")
        return link_clean
    except:
        return ' '

def clean_twitter(url):
    """
    Clean a twitter link of all the http, www, lang=

    Arguments: 
    url: twitter url

    Return:
    clean: cleaned url
    """
    out = ['status']
    if any(x in url for x in out):
        return ' '
    else: 
        http = 'http://twitter.com/'
        https = 'https://twitter.com/'
        clean = url.replace(http, '').replace(https, '')
        return clean

def twitter(artist):
    """
    Get Twitter link for a given artist from Google by searching "artist dj twitter"

    Checks whether it's really a twitter link, if not return empty string.
    Otherwise first link from search is returned.

    Arguments:
    artist: name of the artist
    
    Return: 
    twitter_clean: twitter link of artist
    """    
    artist_google = artist_to_query(artist)
    url = google_url + artist_google + "+dj+twitter"
    soup = get_soup(url)
    try:
        twitter = soup.find("cite").getText()
        artist_check = re.sub('[ ]', '', artist.lower())
        if 'twitter' in twitter:
            if artist_check in twitter:
                twitter_clean = clean_twitter(twitter)
                return twitter_clean
            else: 
                raise ValueError('Artist name not in link!')
        else:
            raise ValueError('Not a Twitter link!')
    except:
        return ' '

def clean_fb(url):
    #TODO Facebook strings
    return url.replace('https://nl-nl.facebook.com/').replace('https://de-de.facebook.com/')

def facebook(artist):

    """
    Get Facebook link for a given artist from Google by searching "artist dj facebook"

    Checks whether it's really a facebook link, if not return empty string.
    Otherwise first link from search is returned.

    Arguments:
    artist: name of the artist
    
    Return: 
    facebook_clean: facebook link of artist
    """    
    artist_fb = artist_to_query(artist)
    url = google_url + artist_fb + "+dj+facebook"
    soup = get_soup(url)
    try:
        facebook = soup.find("cite").getText()
        if 'facebook' in facebook:
            facebook_clean = clean_fb(facebook)
            return facebook_clean
        else:
            raise ValueError('Not a Facebook link!')
    except:
        return ' '

def clean_insta(url):
    """
    Gets rid of unnecessary information in url. 
    If its not an instagram link, or a link which merely tagged the artist return empty string.

    Arguments:
    url: instagram url to be cleaned

    Example: 
    clean_insta(https://www.instagram.com/amelie_lens/?hl=de) -> amlie_lens
    """
    out = ['tags', '/p/', 'pictaram', 'the picta']
    if any(x in url for x in out):
        return ' '
    else: 
        http_w = 'http://www.instagram.com/'
        https_w = 'https://www.instagram.com/'
        http = 'http://instagram.com/'
        https = 'https://instagram.com/'
        clean = url.replace(https_w, '').replace(https, '').replace(http_w, '').replace(https_w, '').replace('?hl=de', '')
        return clean

def instagram(artist):
    """
    Get Instagram link for a given artist from Google by searching "artist dj instagram"

    Checks whether it's really an instagram link, if not return empty string.
    Otherwise first link from search is returned

    Arguments:
    artist: name of the artist

    Return: 
    None
    """
    artist_g = artist_to_query(artist)
    url = google_url + artist_g + "+dj+instagram"
    soup = get_soup(url)
    try:
        instagram = soup.find("cite").getText()
        if 'instagram' in instagram:
            instagram_clean = clean_insta(instagram)
            return instagram_clean
    except:
        return ' '

def partyflock(artist):
    """
    Get the partyflock link of a given artist directly via Partyflock search function

    Arguments:
    artist: name of artist

    Return: 
    link_clean: partyflock link

    Example: 
    partyflock('Adam Beyer') -> 'https://partyflock.nl/artist/190:Adam-Beyer'

    """
    artist_pf = re.sub('[ ]', '+', artist)
    url = partyflock_url + artist_pf
    soup = get_soup_js(url)
    try:
        link_dirty = soup.find('a', id=True)
        link_clean = link_dirty['href']
        return link_clean
    except:
        return ' '

def record_labels(artist):
    """
    Get all the record labels for a given artist from labelsbase.com

    Arguments
    artist: name of the artist

    Return:
    artist_labels_return: string with comma-seperated labels
    """

    artist_query = artist_to_query(artist)
    url = labelbase_url + artist_query
    soup = get_soup(url)
    try:
        for label_div in soup.find_all('div', {'class': 'row label-item'}):
            label_info = label_div.find_all('a', href=True)
            labels.append(label_info[1]['href'])
            artist_labels.append(label_info[1].getText())

        artist_labels_return = ",".join(artist_labels)
        return artist_labels_return

    except:
        return ' '
