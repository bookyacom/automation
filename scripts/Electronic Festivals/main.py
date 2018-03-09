import sys 
import os 

from links import get_links
from scrape_links import scrape_events

file_path = os.getcwd()

if len(sys.argv) != 2: 
    print('Give a Electronic Festivals link from homepage with filter for events to start scraping')
    print('Example: http://www.electronic-festivals.com/home/result?title=&field_genre_tags_tid=All&field_type_of_event_value=All&country=All&date_filter%5Bmin%5D%5Bdate%5D=05/10/2017&date_filter%5Bmax%5D%5Bdate%5D=04/03/2019&field_visitors_value=All&field_age_value=All&field_festicket_shop_value=All&page=')
    sys.exit()

url = sys.argv[1]

event_links = get_links(url)

scrape_events(event_links)