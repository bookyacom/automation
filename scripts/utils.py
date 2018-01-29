import os
import requests
import json
import re
from datetime import datetime

api_url = 'https://admin-api.bookya.com/admin/check?'

def set_up_event (ws):

	"""
    Initialize the Excel File with the Header

    Arguments:
	ws: active Workbook

    Return:
	None
    """

	ws.cell(row=1, column = 1).value = "display_name"
	ws.cell(row=1, column = 2).value = "profile_photo"
	ws.cell(row=1, column = 3).value = "cover_photo"
	ws.cell(row=1, column = 4).value = "email"
	ws.cell(row=1, column = 5).value = "public_email"
	ws.cell(row=1, column = 6).value = "public_contact_number"
	ws.cell(row=1, column = 7).value = "search_artist"
	ws.cell(row=1, column = 8).value = "header_text"
	ws.cell(row=1, column = 9).value = "contact_number"
	ws.cell(row=1, column = 10).value = "bio"
	ws.cell(row=1, column = 11).value = "websites"
	ws.cell(row=1, column = 12).value = "genre_list"
	ws.cell(row=1, column = 13).value = "start_date"
	ws.cell(row=1, column = 14).value = "end_date"
	ws.cell(row=1, column = 15).value = "ticket_price"
	ws.cell(row=1, column = 16).value = "ticket_currency"
	ws.cell(row=1, column = 17).value = "contact_person"
	ws.cell(row=1, column = 18).value = "promoter_name"
	ws.cell(row=1, column = 19).value = "promoter_url"
	ws.cell(row=1, column = 20).value = "venue_name"
	ws.cell(row=1, column = 21).value = "venue_url"
	ws.cell(row=1, column = 22).value = "artist_names"
	ws.cell(row=1, column = 23).value = "artist_urls"
	ws.cell(row=1, column = 24).value = "facebook_page"
	ws.cell(row=1, column = 25).value = "beatport_dj"
	ws.cell(row=1, column = 26).value = "instagram"
	ws.cell(row=1, column = 27).value = "lastfm"
	ws.cell(row=1, column = 28).value = "mixcloud"
	ws.cell(row=1, column = 29).value = "partyflock"
	ws.cell(row=1, column = 30).value = "songkick"
	ws.cell(row=1, column = 31).value = "soundcloud"
	ws.cell(row=1, column = 32).value = "spotify"
	ws.cell(row=1, column = 33).value = "twitter"
	ws.cell(row=1, column = 34).value = "youtube_channel"
	ws.cell(row=1, column = 35).value = "bandsintown"

def get_event_name (soup):
	try:
		return soup.find('h1').string
	except:
		return ''

def line_up(p_tags, problem_artists):
	"""
    Scrape artist names from site and divide them into
	artists that are matched within bookya DB and those who are not

	Arguments:
	p_tags:

	Return values:
	artists_bookya: Artists that are matched in Bookya DB
	artists_notBookya: Artists that aren't matched in Bookya DB
	problem_artists: Artists that have more than one match

	Side Effects:
    """

	try:
		artists_notBookya = []
		artists_bookya = []
		line_up = p_tags[0].find_all('a', href=True)
		for item in line_up:
			artist = item.get_text()
			artist_req = artist.encode('utf-8')
			parameters = {"name": artist_req, "type": "artist"}
			response = requests.get(api_url, params=parameters)
			data = response.json()
			if not data['profiles']:
				artists_notBookya.append(artist)
			else:
				if len(data['profiles']) >= 2:
					artists_bookya.append(artist)
					problem_artists.append(artist)
				else:
					artists_bookya.append(data['profiles'][0]['bookya_url'])

		return artists_notBookya, artists_bookya, problem_artists
	except:
		return [], [], []

def bio (p_tags):
	try:
		bio_ = p_tags[1].get_text()
		bio = bio_.encode('utf-8')
		return bio.strip()
	except:
		return ''

def flyer_picture(soup):
	try:
		fyler_div = soup.find('div', {'class': 'flyer'})
		flyer_dirty= flyer_div.find('a', href=True)
		flyer = "https://www.residentadvisor.net" + flyer_dirty['href']
		return flyer
	except:
		return ''

def dates(a_tags):

	date_start = True
	date_end = False
	formatted_date_1 = ''
	formatted_date_2 = ''
	for item in a_tags:
		try:
			if "events" in item['href'] and date_end:
				time_1 = item.get_text().strip()
				date_1 = datetime.strptime(time_1, '%d %b %Y')
				formatted_date_1 = date_1.strftime('%d/%m/%Y')
				date_end = False
			if "events" in item['href'] and date_start:
				time_2 = item.get_text().strip()
				date_2 = datetime.strptime(time_2, '%d %b %Y')
				formatted_date_2 = date_2.strftime('%d/%m/%Y')
				date_start = False
				date_end = True
		except:
			formatted_date_1 = ''
			formatted_date_2 = ''

	return formatted_date_2, formatted_date_1

def venue(a_tags):
	for item in a_tags:
		try:
			if "club.aspx" in item['href']:
				venue = item.get_text()
				venue_req = re.sub(r'[^a-zA-Z äüöÄÜÖ]+', '', venue)
				venue_temp = venue_req.split()
				if len(venue_temp) >= 3:
					venue_req = venue_temp[0] +' '+ venue_temp[1] +' '+ venue_temp[2]
				parameters = {"name": venue_req, "type": "venue"}
				response = requests.get(api_url, params=parameters)
				data = response.json()
				if not data['profiles']:
					return False, venue
				else:
					return True, data['profiles'][0]['bookya_url']

		except:
			return False, ''

def costs(li):
	cost_found = False
	for item in li:
		try:
			if "Cost" in item.get_text() and not cost_found:
				cost_dirty = item.get_text()
				cost_clean = cost_dirty.replace('Cost /', '')
				if ("€" or "Euro") in cost_clean:
					currency_ = "eur"
					cost_clean = cost_clean.replace('€', '')
				elif "$" in cost_clean:
					currency_ = "$"
					cost_clean = cost_clean.replace('$', '')
				elif "£" in cost_clean:
					currency_ = "£"
					cost_clean = cost_clean.replace('£', '')

				break

			else:
				cost_clean, currency_ = '', ''


		except:
			cost_clean, currency_ = '', ''

	return cost_clean, currency_

def promoter(li):
	for item in li:
		try:
			if "Promoters /" in item.get_text():
				prom_dirty = item.get_text()
				prom_clean1 = prom_dirty.replace('Promoters /', '')
				prom_clean2 = prom_clean1.encode('utf8')
				parameters = {"name": prom_clean2, "type": "promoter"}
				response = requests.get(api_url, params=parameters)
				data = response.json()
				if not data['profiles']:
					return False, prom_clean1
				else:
					return True, data['profiles'][0]['bookya_url']
		except:
			pass

	return False, ''

def fill_eventlist(file_path, file_name):
	return [line.rstrip('\n') for line in open(os.path.join(file_path, file_name), 'r')]
