from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests
import os

def get_soup_js(url):
    """
    Get html and javascript from site and parse it with Beautiful Soup

    Arguments:
    url: URL to be parsed

    Return:
    soup: Parsed html site

    """
    try:
        path_to_chromedriver = '/Users/nequalstim/Desktop/bookya/chromedriver'
        browser = webdriver.Chrome(executable_path = path_to_chromedriver)
        # browser.wait = WebDriverWait(browser, 2)
        browser.get(url)
        # sleep(2)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        browser.close()
        return soup
    except:
        return ''

def get_soup(url):
    """
    Get html from site and parse it with Beautiful Soup

    Arguments:
    url: URL to be parsed

    Return:
    soup: Parsed html site
    """
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")
        return soup
    except:
        return ''
