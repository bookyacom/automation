import sys
sys.path.append('../')

import os

from scrape_links import scrape_links_event

def fill_eventlist(file_path, file_name):
    return [line.rstrip('\n') for line in open(os.path.join(file_path, file_name), 'r')]

if(len(sys.argv) != 2):
    print('Give first cmd line argument: file_name.txt')
    sys.exit()

file_path = os.getcwd()
file_name = sys.argv[1]

#array filled with RA links of events given by user
eventlinks = fill_eventlist(file_path, file_name)

scrape_links_event(eventlinks)
