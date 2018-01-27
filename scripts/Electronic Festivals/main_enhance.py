import sys
from pandas import read_excel
from enhance_matching import matching

if len(sys.argv) < 2: 
    print('Give me an Excel file')
    sys.exit()

frame = read_excel(sys.argv[1])
festivals = frame.values
matching(festivals)