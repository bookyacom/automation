import os
from soup import get_soup

def get_links(url):
    """
    This method grabs all the event links from Electronic Festivals (EF)

    Arguments:
    link: EF link from homepage with filters activated

    Return: 
    links: array filled with Electronic Festivals links
    """

    links = []

    for page_num in range(1,25):

        site = get_soup(url)

        block = site.find_all('div', {'class': 'view-content'})

        for link in block:
            for item in link.find_all('a', href=True):
                if "#" in item['href']:
                    pass
                else:
                    links.append(item['href'])

    return links
