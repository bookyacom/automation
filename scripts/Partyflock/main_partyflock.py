import os
import sys
from links import get_artist_links
from scrape_artist import get_information

file_path = '/Users/nequalstim/Desktop/partyflock'

if len(sys.argv) < 3: 
    print('USAGE: [file_name] [start index] [stop index]')
    sys.exit()


file_name = sys.argv[1]
start  = int(sys.argv[2])
end = int(sys.argv[3])

artist_urls = [line.rstrip('\n') for line in open(os.path.join(file_path, file_name), 'r')]

get_information(artist_urls[start:end])