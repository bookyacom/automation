## Requirements
at least Python 2.7, Python 3.6.3 preferred!

Openpyxl's Workbook [https://openpyxl.readthedocs.io/en/default/]
BeautifulSoup [https://www.crummy.com/software/BeautifulSoup/bs4/doc/]
requests [http://docs.python-requests.org/en/master/]
selenium [http://selenium-python.readthedocs.io/]

Chromedriver  needs to be installed (-> see soup.py/get_soup_js() path to chromedriver) [https://sites.google.com/a/chromium.org/chromedriver/home]

## Get started
USAGE python main_partyflock.py [mode] ([file name])

The Scraper works in two modes, which will be explained in the following.
The difference between them is where they retrieve the partyflock links from. 

    Mode 1

    Scraper will get the links from the Partyflock site by himself and filter out artists, that are already listed in the bookya DB. 

    LAUNCH python main_partyflock.py 1

    Mode 2

    Scraper will retrieve the links from given .txt file and then continue scraping.
    Note: There's a all_artists.txt file in the repository with all artist links scraped in mid January. 

    LAUNCH python main_partyflock.py 2 example.txt