import re
from soup import get_soup

def clean_string(url, site):
    """
    Brings string into right format for Excel file to import 
    (free of https://, www.facebook.com etc., viberate characteristics  )

    Arguments:
    url: url ot be cleaned
    site: site name which will get removed

    Return:
    clean: cleaned string
    """
    http  = 'http://'+site
    https = 'https://'+site
    http_www  = 'http://www.'+site
    https_www = 'https://www.'+site

    clean = url.replace(http, '').replace(https, '').replace(https_www, '').replace(http_www, '')
    clean = clean.replace('Viberate_com', '').replace('viberateOFC/', '')
    return clean

def viberate(artist, ws, row):
    """
    Get all relevant social info for one artist from viberate

    Arguments:
    artist: artist name
    ws: file pointer for excel sheet
    row: row for artist entry

    Side Effects:
    Directly write into the Excel sheet via the given file pointer "ws"

    Return:
    None
    """

    artist_formatted = re.sub('( & )', '-', artist)
    artist_formatted = re.sub('[ ]', '-', artist_formatted)
    url = "https://www.viberate.com/artists/profile/" + artist_formatted

    soup = get_soup(url)

    #check if artist exists on viberate
    test = soup.find('h1')

    if(test['id'] == 'artist-name-title'):
        try:
            dirty_home = soup.find("a", {"title": "Home Page"})
            clean_home = dirty_home['href']
            ws.cell(row=row, column = 2).value = clean_home
        except:
            ws.cell(row=row, column = 2).value = ' '

        try:
            dirty_facebook = soup.find("a", {"title": "Facebook"})
            clean_facebook = clean_string(dirty_facebook['href'], 'facebook.com/')
            ws.cell(row=row, column = 4).value = clean_facebook
        except:
            ws.cell(row=row, column = 4).value = ' '

        try:
            dirty_beatport = soup.find("a", {"title": "Beatport"})
            clean_beatport = clean_string(dirty_beatport['href'],'beatport.com/artist')
            clean_beatport = clean_string(clean_beatport['href'],'pro.beatport.com/artist')
            ws.cell(row=row, column = 5).value = clean_beatport
        except:
            ws.cell(row=row, column = 5).value = ' '

        try:
            dirty_instagram = soup.find("a", {"title": "Instagram"})
            clean_instagram = clean_string(dirty_instagram['href'],'instagram.com/')
            ws.cell(row=row, column = 6).value = clean_instagram
        except:
            ws.cell(row=row, column = 6).value = ' '

        try:
            dirty_mixcloud = soup.find("a", {"title": "Mixcloud"})
            clean_mixcloud = clean_string(dirty_mixcloud['href'], 'mixcloud.com')
            ws.cell(row=row, column = 8).value = clean_mixcloud
        except:
            ws.cell(row=row, column = 8).value = ' '

        try:
            dirty_songkick = soup.find("a", {"title": "Songkick"})
            clean_songkick = clean_string(dirty_songkick['href'], 'songkick.com/artists')
            ws.cell(row=row, column = 10).value = clean_songkick
        except:
            ws.cell(row=row, column = 10).value = ' '

        try:
            dirty_soundcloud = soup.find("a", {"title": "SoundCloud"})
            clean_soundcloud = clean_string(dirty_soundcloud['href'], 'soundcloud.com')
            ws.cell(row=row, column = 11).value = clean_soundcloud
        except:
            ws.cell(row=row, column = 11).value = ' '

        try:
            dirty_spotify= soup.find("a", {"title": "Spotify"})
            clean_spotify = clean_string(dirty_spotify['href'], 'open.spotify.com/' )
            ws.cell(row=row, column = 12).value = clean_spotify
        except:
            ws.cell(row=row, column = 12).value = ' '

        try:
            dirty_twitter = soup.find("a", {"title": "Twitter"})
            clean_twitter = clean_string(dirty_twitter['href'], 'twitter.com/')
            ws.cell(row=row, column = 13).value = clean_twitter
        except:
            ws.cell(row=row, column = 13).value = ' '

        try:
            dirty_youtube = soup.find("a", {"title": "Youtube"})
            clean_youtube = clean_string(dirty_youtube['href'],'youtube.com/')
            ws.cell(row=row, column = 14).value = clean_youtube
        except:
            ws.cell(row=row, column = 14).value = ' '

        try:
            dirty_bands = soup.find("a", {"title": "Bandsintown"})
            clean_bands = clean_string(dirty_bands['href'], 'bandsintown.com')
            ws.cell(row=row, column = 15).value = clean_bands
        except:
            ws.cell(row=row, column = 15).value = ' '

        