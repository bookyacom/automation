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
    cities = ['Moscow', 'London', 'St Petersburg', 'Berlin', 'Madrid', 'Roma', 'Kiev', 'Paris', 'Bucharest', 'Budapest', 'Hamburg', 'Minsk', 'Warsaw', 'Belgrade', 'Vienna', 'Kharkov', 'Barcelona', 'Novosibirsk', 'Nizhny Novgorod', 'Milan', 'Ekaterinoburg', 'Munich', 'Prague', 'Samara', 'Omsk', 'Sofia', 'Dnepropetrovs','Kazan', 'Ufa', 'Chelyabinsk', 'Donetsk', 'Naples', 'Birmingham', 'Perm', 'Rostov-na-Donu', 'Odessa', 'Volgograd', 'Cologne', 'Turin', 'Voronezh', 'Krasnoyarsk','Saratov','Zagreb','Zaporozhye','Lódz','Marseille','Riga','Lvov','Athens','Salonika','Stockholm','Kraków','Valencia','Amsterdam','Leeds','Tolyatti','Kryvy Rig','Sevilla','Palermo','Ulyanovsk','Kishinev','Genova','Izhevsk','Frankfurt am Main','Krasnodar','Breslau','Glasgow','Yaroslave','Khabarovsk','Vladivostok','Zaragoza','Essen','Rotterdam','Irkutsk','Dortmund','Stuttgart','Barnaul','Vilnius','Poznan','Düsseldorf','Novokuznetsk','Lisbon','Lisboa','Helsinki','Málaga','Bremen','Sheffield','Sarajevo','Penza','Ryazan','Orenburg','Naberezhnye Tchelny','Duisburg','Lipetsk','Hannover','Mykolaiv','Tula','Oslo','Tyumen','Copenhagen','Kemerovo','Mariupol','Leipzig','Nuremberg','Bradford','Astrakhan','Dublin','Tomsk','Dresden','Gomel','Liverpool','Anvers','Lugansk','Kirov','Gothenburg','Cheboksary','Ivanovo','Danzig','Bryansk','Tver','Edinburgh','Bratislava','s-Gravenhage','Kursk','Manchester','SKOPLJE','Magnitogorsk','Kaliningrad','Tallin','Szczecin','Lyon','Kaunas','Bristol','Nizhny Tagil','Bochum','Kirklees','Makeyevka','Bydgoszcz','Bologna','Brno','Vinnutsya','Firenze','Murmansk','Ulan-Ude','Wuppertal','Arkhangelsk','Kurgan','Toulouse','Lublin','Mogilev','Kherson','Las Palmas','Smolensk','Bilbao','Sevastopol','Murcia','Fife','Iasi','Katowice','Nice','Stavropol','Constanta','Orel','Catania','Vitebsk','Kaluga','Belgorod','Zürich','Simferopol','Bari','Vladimir','Sochi','Cluj-Napoca','Makhachkala','Galati','Wirral','North Lanarkshire','Timisoara','Cherepovets','Ostrava','Bielefeld','Wakefield','Valladolid','Saransk','Cardiff','Brasov','Craiova','Poltava','Tambov','Dudley','Wigan','Chita','Vladikavkaz','East Riding of Yorkshire','Cherkassy','Mannheim','Córdoba','South Lanarkshire','Chernigov','Coventry','Gorlovka','Palma de Mallorca','Grodno','Bonn','Vologda','Varna','Venezia','Zhitomir','Belfast','Sumy','Leicester','Komsomolsk-na-Amure','Sunderland','Sandwell','Doncaster','Stockport','Sefton','Kostroma','Vigo','Århus','Brest','Volzhsky','Taganrog','Bialystok','Nottingham','Petrozavodsk','Newcastle-upon-Tyne','Gelsenkirchen','Bratsk','Dzerzhinsk ','Surgut','Karlsruhe','Orsk','Porto','Alicante','Dneprodzerzhinsk','Wiesbaden','Kirovograd','Kingston-upon-Hull','Novi Sad','Bolton','Angarsk','Sterlitamak','Münster','Gijón','Ljubljana','Mönchengladbach','Chemnitz','Messina','Walsall','Chernovtsy','Khmelnitsky ','Malmö','Czestochowa','Plymouth','Hospitalet de Llobregat','Rotherham','Augsburg','Stoke-on-Trent','Halle','Verona','Gdynia','Strasbourg','Ploiesti','Nis','Ioshkap-Ola','Braunschweig','Nantes','Wolverhampton','Rovno','Tirana','Aachen','Sosnowiec','Granada','Kosice','Krefeld','Rybinsk','La Coruña','Krementchug','Nizhenvartovsk','Graz','Prokopyevsk','Severodvinsk','South Gloucestershire','Magdeburg','Ivano-Frankovsk','Kiel','Braila','Derby','Utrecht','Ternopol','Radom','Gent','Swansea','Naltchik','Syktivkar','Velikiy Novgorod','Salford','Bergen','Aberdeenshire', 'Socal', 'Miami', 'Sao Paulo', 'Las Vegas','Sopron', 'Perth', 'Sydney', 'Eindhoven', 'Melbourne', 'Auckland', 'Edinburgh', 'San Bernardino', 'Dallas', 'Cape Town', 'New York City', 'Johannesburg', 'Jakarta', 'Brisbane', 'San Francisco', 'Fremantle','Arizona', 'Victoria', 'Nijmegen', 'Tilburg', 'Leysin', 'Groningen', 'Los Angeles', 'Bogotà', 'Tel Aviv', 'Panama City', 'Reykjavík', 'Hong Kong','Lima', 'Cardiff', 'Bendigo', 'Indanapolis', 'Adelaide', 'Columbus', 'Kalamazoo', 'Pittsburgh', 'Saarbrücken', 'Maastricht', 'Brooklyn', 'Denver', 'Detroit', 'Toronto', 'Montreal', 'Buenos Aires', 'Beijing', 'Shanghai', 'Kiel', 'Mumbai', 'Hyderabad', 'Delhi', 'Breda', 'Vermont', 'Brasilia', 'Canberra' ]

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
    festival_req = festival_req.replace('Festival', '')
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

