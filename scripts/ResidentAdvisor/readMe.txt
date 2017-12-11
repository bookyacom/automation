In this repository there are three different scrapers to collect data on Venues, Promoters and Events from ResidentAdvisor (RA). 

The scrapers run on Python3 and the following Librarys must be installed beforehand:
    - [BeautifoulSoup4] (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - [lxml] (http://lxml.de/3.0/)
    - [openpyxl] (https://openpyxl.readthedocs.io/en/default/)
    - [Selenium] (http://selenium-python.readthedocs.io/)
    
USAGE
    Venues: python main_clubs.py 'country name 1' 'country name 2' ...
        --> outputs country_name_venues.xlsx
    Promoters: python main_promoter.py 'country name 1' 'country name 2' ...
        --> outputs country_name_promoters.xlsx

    Events: python main_events.py 'file_name.txt'
    file_name.txt contains RA event links collected by Venue/Promoter scraper
        --> outputs RA_events.xlsx

