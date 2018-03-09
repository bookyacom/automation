"""
This method grabs all the event links from Electronic Festivals

The base_url link has to be modified as it displays a range of events,
depending on the filter.

Return: 
EF_links.txt: File filled with links
"""

import os
from soup import get_soup

#open file
file_path = os.getcwd()
ef_list = open(os.path.join(file_path, 'EF_links.txt'), 'w')

for page_num in range(1,25):
    base_url = "http://www.electronic-festivals.com/home/result?title=&field_genre_tags_tid=All&field_type_of_event_value=All&country=All&date_filter%5Bmin%5D%5Bdate%5D=05/10/2017&date_filter%5Bmax%5D%5Bdate%5D=04/03/2019&field_visitors_value=All&field_age_value=All&field_festicket_shop_value=All&page=" + str(page_num)

    site = get_soup(base_url)

    block = site.find_all('div', {'class': 'view-content'})

    for link in block:
        for item in link.find_all('a', href=True):
            if "#" in item['href']:
                pass
            else:
                ef_list.write(item['href'] + "\n")

ef_list.close()
