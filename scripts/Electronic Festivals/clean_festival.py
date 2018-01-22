import re

def clean_country(festival):
    """
    Removes country name of a festival 

    Arguments:
    festival: name of festival

    Return: 
    festival_: name of festival without country name

    Exmpl: Lollapalooza Argentina -> Lollapalooza
    """

    countries = ['United States','Afghanistan','Albania','Algeria','American Samoa','Andorra','Angola','Anguilla','Antarctica','Antigua And Barbuda','Argentina','Armenia','Aruba','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia','Bosnia And Herzegowina','Botswana','Bouvet Island','Brazil','Brunei Darussalam','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Cayman Islands','Central African Rep','Chad','Chile','China','Christmas Island','Cocos Islands','Colombia','Comoros','Congo','Cook Islands','Costa Rica','Cote D`ivoire','Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Falkland Islands (Malvinas)','Faroe Islands','Fiji','Finland','France','French Guiana','French Polynesia','French S. Territories','Gabon','Gambia','Georgia','Germany','Ghana','Gibraltar','Greece','Greenland','Grenada','Guadeloupe','Guam','Guatemala','Guinea','Guinea-bissau','Guyana','Haiti','Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea (North)','Korea (South)','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macau','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Martinique','Mauritania','Mauritius','Mayotte','Mexico','Micronesia','Moldova','Monaco','Mongolia','Montserrat','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','Netherlands Antilles','New Caledonia','New Zealand','Nicaragua','Niger','Nigeria','Niue','Norfolk Island','Northern Mariana Islands','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Pitcairn','Poland','Portugal','Puerto Rico','Qatar','Reunion','Romania','Russian Federation','Rwanda','Saint Kitts And Nevis','Saint Lucia','St Vincent/Grenadines','Samoa','San Marino','Sao Tome','Saudi Arabia','Senegal','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','Spain','Sri Lanka','St. Helena','St.Pierre','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syrian Arab Republic','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tokelau','Tonga','Trinidad And Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','Uruguay','Uzbekistan','Vanuatu','Vatican City State','Venezuela','Viet Nam','Virgin Islands (British)','Virgin Islands U.S.)','Western Sahara','Yemen','Yugoslavia','Zaire','Zambia','Zimbabwe']

    for country in countries:
        if re.search(re.escape(country), festival):
            festival_ = festival.replace(country, '')
            return festival_

    return festival

def clean_city(festival):
     """
    Removes country name of a festival 

    Arguments:
    festival: name of festival

    Return: 
    festival_: name of festival without country name

    Exmpl: Lollapalooza Argentina -> Lollapalooza
    """

    cities =[]

    for city in cities:
        if re.search(re.escape(city), festival):
            festival_ = festival.replace(city, '')
            return festival_

    return festival

def clean_festival(festival):
    """
    Cleans the festival string before making a request to the Bookya DB
    -> higher matching 

    Arguments: 
    festival: name of festival

    Return:
    festival_req: name of festival free of country, city name and "festival"
    """

    festival_req = festival.replace('festival', '')
    festival_req = festival_req.replace('-', '')
    festival_req = festival_req.replace('Winter', '')
    festival_req = festival_req.replace('Summer', '')
    festival_req = festival_req.replace('Indoor', '')
    festival_req = festival_req.replace('Special', '')
    festival_req = festival_req.replace('Edition', '')
    festival_req = festival_req.replace('Music', '')
    festival_req = festival_req.replace('Night', '')
    festival_req = festival_req.replace('Day', '')

    festival_req = clean_country(festival_req)

    return festival_req

