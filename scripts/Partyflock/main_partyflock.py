import os
import sys
from links import get_artist_links
from scrape_artist import get_information

file_path = os.getcwd()

mode = sys.argv[1]

#mode 1 all artist links will be freshly scraped
if mode == "1":
    arist_urls = get_artist_links()

#mode 2 user already gives in file with urls
elif mode == "2":
    if len(sys.argv) < 3: 
        print('USAGE: [mode=2] [file_name]')
        sys.exit()

    file_name = sys.argv[2]
    artist_urls = [line.rstrip('\n') for line in open(os.path.join(file_path, file_name), 'r')]
else:
    print('unknown mode')
    print('USAGE: [mode] ([file_name])')
    sys.exit()

get_information(artist_urls)