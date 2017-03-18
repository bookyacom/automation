In this repository there are three different scrapers to scrape data on Venues, Promoters and Events from ResidentAdvisor (RA). 

The scrapers run on Python 2.7 and the following Librarys must be installed beforehand:
    - BeautifoulSoup4 (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - lxml (http://lxml.de/3.0/)
    - openpyxl (https://openpyxl.readthedocs.io/en/default/)
    
USAGE: 
  1. Change COUNTRY (via multiselection) to desired location 
  2. Copy Paste the corresponding countryID and listend (Venue or Promoter) from RA_IDlist.txt
  3. Mofify filepath 

The Venue and Promoter Scraper will output the following: 
  - COUNTRY.xlsx            --> The "master" excel file with a list of all the venues/promoters and relevant information
  - COUNTRY_ven_links       --> a txt file including the RA venue links 
  - COUTNRY_promlinks       --> a txt file including the RA promoter links
  - COUNTRY_eventlinks      --> a txt file including all the event links listed by collected venues
  - COUNTRY_promeventlinks  --> a txt file including all the event links listed by collected promoters
  
The last two txt files are especially important, because they are used as INPUT for the Event Scraper, which will just 
output an excel file. 
