import sys
import pandas

def initList (ws):
    #initialitze table with values
    ws.cell(row=1, column = 1).value = "dispay_name"
    ws.cell(row=1, column = 2).value = "promoter_name"
    ws.cell(row=1, column = 3).value = "promoter_url"

def matching(festivals):
    """
    Check bookya DB for matching promoter and fill into Excel sheet

    Arguments: 
    festivals: array with festival names

    Side Effects:
    Create Excel file and fill with relevant information

    Return: 
    None
    """

    wb = Workbook()
    filename = 'Enhanced_matching.xlsx'
    ws = wb.active
    ws.title = 'Enhance_matching'
    file_path = '/Users/nequalstim/Desktop/'

    initList(ws)

    for festival_ in festivals:
        festival = clean_festival(festival_)
        

def read_festivals_from_excel(filename): 
    """
    Reads festival names from given Excel file into an array
    File must have 'display_name' column! 
    Arguments: 
    filename: name of Excel file
    
    Return:
    festivals: array of festival names
    """
    df = read_excel(filename)
    festivals = df['display_name'].values
    return festivals

if len(sys.argv) < 2: 
    print('Give me an excel file with festivals in display_name column')
    sys.exit()

festivals = read_artists_from_excel(sys.argv[1])

matching(festivals)