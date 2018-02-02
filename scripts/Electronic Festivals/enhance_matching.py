import sys
import os
from clean_festival import clean_festival
from openpyxl import Workbook
from helper import *
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

def check_db(festival, req_name, result_db):
    """
    Will Match a festival in the bookya DB based on: 
        1. name of festival
        2. website
        3. concepts
        4. country
    Festival has to fulfill one of the three criteria! 

    Arguments
    festival: array of festival info
    req_name: cleaned festival name for request
    result_db: result from the bookya DB for a given festival
    
    Side effects:
    write promoter_url and name into festival array

    Return: 
    festival: updated array
    True: One of the criteria was fulfilled
    False: No criteria fulfilled
    """

    # No matching in the database
    try:
        if not result_db['profiles']:
            festival[15] = ' '
            festival[16] = ' '
            return False, festival
    except: 
        return False, festival
    try: 
        if type(festival[8]) is str:
            website = festival[8]
            for result in result_db['profiles']:
                if fuzz.partial_ratio(website, result['website']) > 85:
                    festival[15] = result['name']
                    festival[16] = result['bookya_url']
                    return True, festival
    except: 
        pass

    try:
        for result in result_db['profiles']:
            if fuzz.partial_ratio(req_name, result['name']) > 90:
                festival[15] = result['name']
                festival[16] = result['bookya_url']
                return True, festival
            for concept in result['concepts'].split(','):# maybe cut string at comma here 
                if fuzz.partial_ratio(req_name, concept) > 90:
                    festival[15] = result['name']
                    festival[16] = result['bookya_url']
                    return True, festival
    except:
        pass

    if type(festival[18]) is str:
        country = festival[18]
        for result in result_db['profiles']:
            if fuzz.partial_ratio(country, result['country']) > 95:
                festival[15] = result['name']
                festival[16] = result['bookya_url']
                return True, festival

    return False, festival

def problem_djs(festival, no, multiple):
    """
    writes DJ names with more than one match in Bookya DB to fp

    Arguments:
    festival: array of festival info
    multiple: Array for djs with multiple matches
    no: array for djs with no match

    Side effects: 
    write into artist_names_comma_seperated and artist_url
    
    DJs either have: 
        - no match
        - exactly one match 
        - more than one match

    DJs with exactly one match will be written in the url column
    DJs with no match will only be in artist_comma_seperated
    DJs with more matches will be in both, so it's easier to replace their names with url 
    when manually checking

    Return:
    festival: updated array
    """

    artist_names = []
    artist_urls = []
    all_matched = True

    if type(festival[19]) is str:
        for dj in festival[19].split(','):
            dj = dj.lower()
            result = request_db(dj, 'artist')
            #DJ has no match in the DB 
            if not result['profiles']:
                artist_names.append(dj)
                no.append(dj)
            #DJ got matched with himself
            elif len(result['profiles']) == 1:
                artist_urls.append(result['profiles'][0]['bookya_url'])
            #DJ has more than one match
            else:
                found = False
                factor = 0
                for index, arti in enumerate(result['profiles']):
                    ratio = fuzz.ratio(dj, arti['name']) 
                    if ratio >= 75 and ratio > factor:
                        factor = ratio
                        found = True
                        artist_index = index

                if found:
                    artist_urls.append(result['profiles'][artist_index]['bookya_url'])
                else:
                    all_matched = False
                    artist_names.append(dj)
                    artist_urls.append(dj)
                    multiple.append(dj)

        festival[19] = ','.join(artist_names)
        festival[20] = ','.join(artist_urls)

        return all_matched, festival

    else:
        return False, festival


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
    Match.xlsx -> found promoter in DB 
    No_Match.xlsx -> didn't find promoter or was unclear

    Return: 
    None
    """

    perfect_match, perfect_match_wb = create_excel('perfect match')
    match, match_wb = create_excel('match')
    no_match, no_match_wb = create_excel('no_match')

    file_path = '/Users/nequalstim/Desktop/Rd2/'

    initList(perfect_match)
    initList(match)
    initList(no_match)

    row_match = 1
    row_no_match = 1
    row_perfect = 1

    no = []
    multiple = []

    for festival in festivals:
        display_name = festival[0]
        req_name = clean_festival(display_name)
        result_db = request_db(req_name, 'promoter')
        got_matched, festival_update = check_db(festival, req_name, result_db)

        if got_matched:
            all_matched, festival_update = problem_djs(festival_update, no, multiple)
            if all_matched:
                row_perfect += 1
                write_to_excel(perfect_match, festival_update, row_perfect)
            else:
                row_match += 1
                write_to_excel(match, festival_update, row_match)
        else: 
            row_no_match += 1
            allmatched, festival_update = problem_djs(festival_update, no, multiple)
            write_to_excel(no_match, festival_update, row_no_match)

    #write problematic DJs to file
    dj_file_no = open(os.path.join(file_path, "DJ_no_match.txt"), 'w')
    dj_file_multiple = open(os.path.join(file_path, "DJ_more_matches.txt"), 'w')

    no = list(set(no))
    multiple = list(set(multiple))

    write_to_file(no, dj_file_no)
    write_to_file(multiple, dj_file_multiple)


    match_wb.save(file_path+'Rd2match.xlsx')
    perfect_match_wb.save(file_path+'Rd2perfect_match.xlsx')
    no_match_wb.save(file_path+'Rd2no_match.xlsx')