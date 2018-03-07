def clean_url(url, site):
    """
    Brings string into right format for Excel file to import 
    (free of https://, www.facebook.com etc.)

    Arguments:
    url: url to be cleaned
    site: site name which will get removed

    Return:
    clean: cleaned string

    e.g. clean_url('https://www.facebook.com/adambeyer', 'facebook') -> adambeyer
    """
    http  = 'http://'+site
    https = 'https://'+site
    http_www  = 'http://www.'+site
    https_www = 'https://www.'+site

    clean = url.replace(http, '').replace(https, '').replace(https_www, '').replace(http_www, '')
    return clean.strip()

"""
All of the following functions take in the string retrieved from Partyflock 
and get rid of unnecessary information, mostly a description of the url 
such as 'facebookpage ' or 'spotify '

Argument:
url: url retrieved from partyflock

Return:
*_link: cleaned link for Excel sheet
"""

def facebook(url):
    fb_link = url.replace('facebookpage: ', '')
    fb_link = fb_link.replace('facebook: ', '')
    fb_link = clean_url(fb_link, 'facebook.com/')
    return fb_link

def soundcloud(url):
    sc_link = url.replace('soundcloud: ', '')
    sc_link = clean_url(sc_link, 'soundcloud.com/')
    return sc_link

def twitter(url):
    twitter_link = url.replace('twitter: ', '')
    twitter_link = clean_url(twitter_link, 'twitter.com/')
    return twitter_link

def youtube(url):
    youtube_link = url.replace('youtube: ', '')
    youtube_link = clean_url(youtube_link, 'youtube.com/')
    return youtube_link

def instagram(url):
    insta_link = url.replace('instagram: ', '')
    insta_link = clean_url(insta_link, 'instagram.com/')
    return insta_link

def spotify(url):
    spotify_link = url.replace('spotify: ', '')
    spotify_link = clean_url(spotify_link, 'open.spotify.com/')
    return spotify_link
