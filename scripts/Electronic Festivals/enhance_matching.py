from clean_festival import clean_festival
from openpyxl import Workbook
from helper import *

def check_db(festival, result_db):
    """
    Will Match a festival in the bookya DB based on: 
        1. name of festival
        2. website
        3. concepts
        4. country
    Festival has to fulfill one of the three criteria! 

    Arguments
    festival: array of festival info
    result_db: result from the bookya DB for a given festival
    
    Side effects:
    write promoter_url and name into festival array

    Return: 
    True
    False
    """

    name = festival[0]
    website = festival[8]
    country = festival[19]

    # No matching in the database
    if not result_db['profiles']:
        del festival[15]
        del festival[16]
        return False
    
    for result in result_db['profiles']:
        if fuzz.partial_ratio(website, result['website']) > 85:
            festival[15] = result['name']
            festival[16] = result['bookya_url']
            return True

    for result in result_db['profiles']:
        if fuzz.partial_ratio(name, result['name']) > 90:
            festival[15] = result['name']
            festival[16] = result['bookya_url']
            return True
        for concept in result['concepts']:# maybe cut string at comma here 
            if fuzz.partial_ratio(name, concept) > 90:
                festival[15] = result['name']
                festival[16] = result['bookya_url']
                return True

    for result in result_db['profiles']:
        if fuzz.partial_ratio(country, result['country']) > 90:
            festival[15] = result['name']
            festival[16] = result['bookya_url']
            return True


def matching(festivals):
    """
    Check bookya DB for matching promoter and fill into Excel sheet
    1. Clean the festival name of any string that might hinder request
    2. Make request to bookya DB 
    3. Check if result is a match with the inout festival
    4. Write to match or no match Excel file

    Arguments: 
    festivals: array with festival info

    Side Effects:
    Create Excel file and fill with relevant information

    Return: 
    None
    """

    match, match_wb = create_excel('match')
    no_match, no_match_wb = create_excel('no_match')

    file_path = '/Users/nequalstim/Desktop/'

    initList(match)
    initList(no_match)

    row_1 = 1
    row_2 = 1

    for festival in festivals:
        display_name = festival[0]
        req_name = clean_festival(display_name)
        result_db = request_db(req_name)
        got_matched = check_db(festival, result_db)

        if got_matched:
            row_1 += 1
            write_to_excel(match, festival, row_1)
        else: 
            row_2 += 1
            write_to_excel(no_match, festival, row_2)

    match_wb.save(file_path+'match.xlsx')
    no_match_wb.save(file_path+'no_match.xlsx')