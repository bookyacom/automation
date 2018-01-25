from soup import get_soup_js
import requests

#partfyflock url 
partyflock_url = 'https://partyflock.nl/artist/'
api_url = 'https://admin-api.bookya.com/admin/check'


def get_artist_links():
    """
    Collects the artist urls from Partyflock which are not listed in the bookya database.

    Arguments: None

    Returns:
    artist_urls: array filled with partyflock artist urls that are not in bookya DB
    """
    indices = ['other', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t' ,'u', 'v', 'w', 'x', 'y', 'z']

    artist_urls = []

    for index in indices:
        soup = get_soup_js(partyflock_url+index)
        artists = soup.find_all('a', id=True)
        for artist in artists: 
            name = artist.getText()
            if not artist_on_bookya(artist):
                artist_url = artist['href']
                artist_urls.append(artist_url)

    return artist_urls

def artist_on_bookya(artist):
    """
    Checks if artist is in the Bookya database

    Arguments: 
    artist: name of artist

    Return 
    True: Artist is in database
    False: Artist is not in database
    """

    try:
        artist_req = artist.encode('utf-8')
        parameters = {"name": artist_req, "type": "artist"}
        response = requests.get(api_url, params=parameters)
        data = response.json()
        if data['profiles']:
            return True
        else: 
            return False
    except:
        return False
