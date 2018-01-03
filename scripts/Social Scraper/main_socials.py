from pandas import read_excel
import sys
from scrape_artists import scrape_artists

def read_artists_from_excel(filename): 
    """
    Reads artist names from given Excel file into an array
    File must have 'display_name' column! 

    Arguments: 
    filename: name of Excel file
    
    Return:
    artists_names: array filled with artist names
    """
    df = read_excel(filename)
    artist_names = df['display_name'].values
    return artist_names


if len(sys.argv) < 2: 
    print('Give me an excel file with artists in display_name column')
    sys.exit()

artists = read_artists_from_excel(sys.argv[1])


scrape_artists(artists)