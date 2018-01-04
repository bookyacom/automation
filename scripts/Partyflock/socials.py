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

    presence_row = artist_page.find('tr', {'class': 'presencerow'})
    social_links = presence_row.find_all('a', title=True)
    
    for link in social_links:
        social_info = link['title']

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

def get_website(artist_page, ws, row):
    """
    """


def get_bio(artist_page, ws, row):
    """
    Get the Bio of a given artist page on Partyflock


    """
    #TODO: Cut out Biografie and Date
    try: 
        bio_ = artist_page.find('div', {'id': 'biobody'} )
        bio = bio_.getText()
        print('bio 1')
    except: 
        try:
            bio_ = artist_page.find('article', {'data-partyflock-type': 'bio'})
            bio = bio_.getText()
            print(bio)
        except:
            pass

def clean_url(url, site):
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
    return clean.strip()

def facebook (url):
    fb_link = url.replace('facebookpage: ', '')
    fb_link = clean_url(fb_link, 'facebook.com/')
    return fb_link

def soundcloud (url):
    sc_link = url.replace('soundcloud: ', '')
    sc_link = clean_url(sc_link, 'soundcloud.com/')
    return sc_link

def twitter (url):
    twitter_link = url.replace('twitter: ', '')
    twitter_link = clean_url(twitter_link, 'twitter.com/')
    return twitter_link

def youtube (url):
    youtube_link = url.replace('youtube: ', '')
    youtube_link = clean_url(youtube_link, 'youtube.com/')
    return youtube_link

def instagram (url):
    insta_link = url.replace('instagram: ', '')
    insta_link = clean_url(insta_link, 'instagram.com/')
    return insta_link

def spotify (url):
    spotify_link = url.replace('spotify: ', '')
    spotify_link = clean_url(spotify_link, 'open.spotify.com/')
    return spotify_link

