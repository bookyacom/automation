## Requirements
at least Python 2.7, Python 3.6.3 preferred!

[Openpyxl's Workbook](https://openpyxl.readthedocs.io/en/default/) \n
[BeautifulSoup]([https://www.crummy.com/software/BeautifulSoup/bs4/doc/]) \n
[requests]([http://docs.python-requests.org/en/master/]) \n
[selenium]([http://selenium-python.readthedocs.io/]) \n

Chromedriver  needs to be installed (-> see soup.py/get_soup_js() path to chromedriver) [Chrome](https://sites.google.com/a/chromium.org/chromedriver/home)

## Get started
    There are three scrapers in this repository 

    1. Venues

    LAUNCH python3 main_venues.py [countries]

    This scraper will first collect all the links of the venues in a given country and then start \n scraping them, if the venue is still alive (had to have an event in 2016/17/18).\n
    Further, it extracts all the event links from the venues and outputs them in a .txt file \n for later scraping. 

    2. Promoters

    LAUNCH python3 main_promoters.py [countries]

    Essentially does the same thing, just for promoters of given countries


    3. Events

    You have to feed this scraper a .txt file containing RA event links as collected above. \n
    It will then gather all the information from the site. Promoter, Venue and DJs will be matched \n directly within the Bookya DB. If the scraper finds a DJ with multiple matches it will write \n it to problem_artists.txt, a file outputted at the end. 