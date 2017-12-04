from bs4 import BeautifulSoup
import os
from time import sleep
import re
from datetime import datetime
import requests

api_url = 'https://admin-api.bookya.com/admin/check?'

def name(soup):
    """
    Extracts the name of a club/promoter/event listing

    Arguments:
    soup: Page of the club/promoter/event parsed with BS

    Return:
    name: utf-8 encoded name
    """
    try:
        event_name = soup.find('h1').string.encode('utf-8')
        return event_name
    except:
        return ' '

def bio(soup):
    """
    Extracts the biography of a club listing

    Arguments:
    soup: Page of the club parsed with BS

    Return:
    bio: utf-8 encoded biography
    """
    try:
        bio_dirty = soup.find('div', {'class': 'pr24 pt8'})
        bio = bio_dirty.get_text()
        bio = bio.encode('utf8')
        if not len(bio):
            return ' '
        return bio
    except:
        return ' '

def bio_event (p_tags):
    try:
        bio_ = p_tags[1].get_text()
        bio = bio_.encode('utf-8')
        return bio.strip()
    except:
        return ''

def address(soup):
    """
    Extract the Address of a club listing


    Arguments:
    soup: Page of the club parsed with BS

    Return:
    address: utf-8 encoded address of club
    """
    try:
        address_dirty = soup.find('span', {'itemprop': 'street-address'})
        address = address_dirty.get_text()
        address = address.encode('utf-8')

        return address
    except:
        return ' '

def picture(soup):
    """
    Extract the Picture of a club/promoter listing

    Arguments:
    soup: Page of the club/promoter parsed with BS

    Return:
    picture: link of picture
    """
    try:
        picture_div = soup.find('div', {'class': 'fl col2 pb64'})
        picture_dirty = picture_div.find('img', src=True)
        picture = "https://www.residentadvisor.net" + picture_dirty['src']
        return picture
    except:
        return ' '

def flyer_picture(soup):
    """
    Extract the Flyer Picture of an event listing

    Arguments:
    soup: Page of the event parsed with BS

    Return:
    picture: link of fyler picture
    """
    try:
        fyler_div = soup.find('div', {'class': 'flyer'})
        flyer_dirty= flyer_div.find('a', href=True)
        flyer = "https://www.residentadvisor.net" + flyer_dirty['href']
        return flyer
    except:
        return ''

def homepage(sites):
    """
    Extract the Website (which can be a FB link) of a club listing

    Arguments:
    sites: all links in top_bar of club listing

    Return:
    website: link to website
    facebook: link to facebook_page of club
    """
    try:
        website = ' '
        facebook = ' '
        for site in sites:
            if "Website" in site.get_text():
                link = site['href']
                if "facebook" in link:
                    facebook = link
                else:
                    website = link
            elif "Facebook" in site.get_text():
                link = site['href']
                facebook = link

        return website, facebook
    except:
        return ' ', ' '

def mail(sites):
    """
    Extract the Email of a club listing

    Arguments:
    sites: all links in top_bar of club listing

    Return:
    email: email of club
    """
    try:
        for site in sites:
            if "Email" in site:
                email_dirty = site['href']
                email = email_dirty.replace("mailto:", "")
        return email
    except:
        return ' '

def capacity(top_bar):
    """
    Extract the Capacity of a club listing

    Arguments:
    top_bar: top_bar of club listing containing relevant info

    Return:
    Capacity: capacity of a club or ' ' if not given
    """
    try:
        li_items = top_bar.find_all('li')
        for li in li_items:
            if "Capacity" in li.get_text():
                capacity_dirty = li.get_text()
                capacity = capacity_dirty.replace("Capacity /", "")
                return capacity
        return ' '
    except:


        return ' '

def phone(top_bar):
    """
    Extract the Phone number of a club listing

    Arguments:
    top_bar: top_bar of club listing containing relevant info

    Return:
    phone: Phone of a club or ' ' if not given
    """
    try:
        li_items = top_bar.find_all('li')
        for li in li_items:
            if "Phone" in li.get_text():
                phone_dirt = li.get_text()
                phone = phone_dirt.replace("Phone /", "")
                return phone
        return ' '
    except:
        return ' '

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

def placeholders(ws,y):
    """
    Sets empty cells to " " for nicer formatting in Excel

    Arguments:
    ws: Workbook
    y: row counter

    Return:
    None

    Side Effect:
    Set the empty cells to " "
    """
    placeholders = [4, 6, 10, 11, 12, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26]
    for column in placeholders:
        ws.cell(row = y, column = column).value = " "

def get_events(soup, events):
    """
    Extract all the event links from a given venue

    Arguments:
    soup: Page of the club parsed with BS
    events: Array

    Return:
    None

    Side Effect:
    Fill up events array with events from different clubs
    """
    for link in soup.find_all('a', href=True):
        if '/events/' in link['href']:
            event = "https://www.residentadvisor.net" + link['href']
            events.append(event)

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

def write_to_file(array, fp):
    for item in array:
        fp.write(item+'\n')

    fp.close()
