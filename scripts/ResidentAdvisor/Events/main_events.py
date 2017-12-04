import sys
sys.path.append('../')

import os

from scrape_links import scrape_links_event

def fill_eventlist(file_path, file_name):
    return [line.rstrip('\n') for line in open(os.path.join(file_path, file_name), 'r')]

file_path = '/Users/nequalstim/Desktop/bookya/temp'

eventlinks = fill_eventlist(file_path, 'test_events.txt')

scrape_links_event(eventlinks)
