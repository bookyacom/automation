import sys
sys.path.append('../')

import os

from scrape_links import scrape_links_event

def fill_eventlist(file_path, file_name):
    return [line.rstrip('\n') for line in open(os.path.join(file_path, file_name), 'r')]

if(len(sys.argv) != 2):
	print('Give first cmdline argument: file_name.txt')
	sys.exit()

file_path = '/Users/nequalstim/Desktop/bookya/temp'
file_name = sys.argv[1]


eventlinks = fill_eventlist(file_path, file_name)

scrape_links_event(eventlinks)
