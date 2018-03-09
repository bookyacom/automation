## Requirements
at least Python 2.7, Python 3.6.3 preferred!

[Openpyxl's Workbook](https://openpyxl.readthedocs.io/en/default/)

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[requests](http://docs.python-requests.org/en/master/)

[selenium](http://selenium-python.readthedocs.io/)

Chromedriver  needs to be installed (-> see soup.py/get_soup_js() path to chromedriver) [Chrome](https://sites.google.com/a/chromium.org/chromedriver/home)

## Get started
This scraper collects social media information on a given list of artists. 
List needs to be in .xlsx format and contain the column 'display_name' with artist names in it. 

Start the scraper by running 

    python main_socials "data_file.xlsx"

and it will output "DJ_Socials.xlsx". 

The scraper will first try to get data from Viberate and if artist is not listed there, continue to collect the main socials (Facebook, Labels, Instagram and Twitter) on its own.