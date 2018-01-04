from soup import get_soup_js
from socials import *

partyflock_url = 'https://partyflock.nl/artist/'

def init_artist_profiles(ws):
    ws.cell(row=1, column = 1).value = 'display_name'
    ws.cell(row=1, column = 2).value = 'websites'
    ws.cell(row=1, column = 3).value = 'record_labels'
    ws.cell(row=1, column = 4).value = 'facebook_page'
    ws.cell(row=1, column = 5).value = 'beatport_dj'
    ws.cell(row=1, column = 6).value = 'instagram'
    ws.cell(row=1, column = 7).value = 'lastfm'
    ws.cell(row=1, column = 8).value = 'mixcloud'
    ws.cell(row=1, column = 9).value = 'partyflock'
    ws.cell(row=1, column = 10).value = 'songkick'
    ws.cell(row=1, column = 11).value = 'soundcloud'
    ws.cell(row=1, column = 12).value = 'spotify'
    ws.cell(row=1, column = 13).value = 'twitter'
    ws.cell(row=1, column = 14).value = 'youtube_channel'
    ws.cell(row=1, column = 15).value = 'bandsintown'

def get_information(artist_urls):
    """

    """

    wb = Workbook()
    filename = 'Partyflock_artists.xlsx'
    ws = wb.active
    ws.title = 'Partyflock'
    file_path = '/Users/nequalstim/Desktop/'

    init_artist_profiles(ws)

    for row, artist_url in enumerate(artist_urls, start=2): 
        artist_page = get_soup_js(partyflock_url + artist_url)

        # Get all the social information
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

    wb.save(file_path + '/Partyflock.xlsx')
