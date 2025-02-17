#!/usr/bin/env python
'''
Appendix F. Grid Mappings
---
Each recognized grid mapping is described in one of the sections below. Each
section contains: the valid name that is used with the grid_mapping_name
attribute; a list of the specific attributes that may be used to assign values
to the mapping's parameters; the standard names used to identify the coordinate
variables that contain the mapping's independent variables; and references to
the mapping's definition or other information that may help in using the
mapping. Since the attributes used to set a mapping's parameters may be shared
among several mappings, their definitions are contained in a table in the final
section. The attributes which describe the ellipsoid and prime meridian may be
included, when applicable, with any grid mapping.

The grid_mapping_attr_types* dictionaries relate type and condition information
for each of the grid_mapping attributes as defined in the CF standard. Each key-
value pair is comprised of

    <attribute name> : {type: S|N|D, extra_condition: True|False}

where the 'type' signifies the type that the attribute should be, and the
'extra_condition' boolean indicates whether to test for an additional condition
or series of conditions to determine if the value of the attribute is valid.

The grid_mapping_dict* dictionaries map the names of grid mappings to an array
of length 1, 3, or 4. The array is comprised of tuples:

    [
        tuple of required attributes,
        tuple of something that is unclear, (often nothing)
        tuple of expected standard names,
        tuple of exclusive attributes

    ]

We have used the FGDC "Content Standard for Digital Geospatial Metadata" [FGDC]
as a guide in choosing the values for grid_mapping_name and the attribute names
for the parameters describing map projections.
'''

grid_mapping_attr_types16 = {
    'earth_radius': {'type': 'N', 'extra_condition': False},
    'false_easting': {'type': 'N', 'extra_condition': False},
    'false_northing': {'type': 'N', 'extra_condition': False},
    'grid_mapping_name': {'type': 'S', 'extra_condition': False},
    'grid_north_pole_latitude': {'type': 'N', 'extra_condition': False},
    'grid_north_pole_longitude': {'type': 'N', 'extra_condition': False},
    'inverse_flattening': {'type': 'N', 'extra_condition': False},
    'latitude_of_projection_origin': {'type': 'N', 'extra_condition': True},
    'longitude_of_central_meridian': {'type': 'N', 'extra_condition': True},
    'longitude_of_prime_meridian': {'type': 'N', 'extra_condition': True},
    'longitude_of_projection_origin': {'type': 'N', 'extra_condition': True},
    'north_pole_grid_longitude': {'type': 'N', 'extra_condition': False},
    'perspective_point_height': {'type': 'N', 'extra_condition': False},
    'scale_factor_at_central_meridian': {'type': 'N', 'extra_condition': True},
    'scale_factor_at_projection_origin': {'type': 'N', 'extra_condition': True},
    'semi_major_axis': {'type': 'N', 'extra_condition': False},
    'semi_minor_axis': {'type': 'N', 'extra_condition': False},
    'standard_parallel': {'type': 'N', 'extra_condition': True},
    'straight_vertical_longitude_from_pole': {'type': 'N', 'extra_condition': True}
}

grid_mapping_attr_types17 = grid_mapping_attr_types16.copy() # need shallow copy; update() returns None

grid_mapping_attr_types17.update({
    'azimuth_of_central_line': {'type': 'N', 'extra_condition': False},
    'crs_wkt': {'type': 'S', 'extra_condition': False},
    'geographic_crs_name': {'type': 'S', 'extra_condition': False},
    'geoid_name': {'type': 'S', 'extra_condition': False},
    'geopotential_datum_name': {'type': 'S', 'extra_condition': False},
    'horizontal_datum_name': {'type': 'S', 'extra_condition': True},
    'prime_meridian_name': {'type': 'S', 'extra_condition': True},
    'projected_crs_name': {'type': 'S', 'extra_condition': True},
    'reference_ellipsoid_name': {'type': 'S', 'extra_condition': False},
    'towgs84': {'type': 'N', 'extra_condition': True}
    })


grid_mapping_dict16 = {
    'albers_conical_equal_area': [
        (
            'longitude_of_central_meridian',
            'latitude_of_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ],
    'azimuthal_equidistant': [
        (
            'longitude_of_projection_origin',
            'latitude_of_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ],
    'lambert_cylindrical_equal_area': [
        (
            'longitude_of_central_meridian'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        ),
        (
            'standard_parallel',
            'scale_factor_at_projection_origin'
        )
    ],
    'lambert_azimuthal_equal_area': [
        (
            'longitude_of_projection_origin',
            'latitude_of_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ],
    'lambert_conformal_conic': [
        (
            'standard_parallel',
            'longitude_of_central_meridian',
            'latitude_of_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ],
    'latitude_longitude': [
        (),
        (),
        (
            'longitude',
            'latitude'
        )
    ],
    'mercator': [
        (
            'longitude_of_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        ),
        (
            'standard_parallel',
            'scale_factor_at_projection_origin'
        )
    ],
    'orthographic': [
        (
            'longitude_of_projection_origin',
            'latitude_of_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ],
    'polar_stereographic': [
        (
            'straight_vertical_longitude_from_pole',
            'latitude_of_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        ),
        (
            'standard_parallel',
            'scale_factor_at_projection_origin'
        )
    ],
    'rotated_latitude_longitude': [
        (
            'grid_north_pole_latitude',
            'grid_north_pole_longitude'
        ),
        (
            'north_pole_grid_longitude'
        ),
        (
            'grid_latitude',
            'grid_longitude'
        )
    ],
    'stereographic': [
        (
            'longitude_of_projection_origin',
            'latitude_of_projection_origin',
            'scale_factor_at_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ],
    'transverse_mercator': [
        (
            'scale_factor_at_central_meridian',
            'longitude_of_central_meridian',
            'latitude_of_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ],
    'vertical_perspective': [
        (
            'longitude_of_projection_origin',
            'latitude_of_projection_origin',
            'perspective_point_height'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ]
}

grid_mapping_dict17 = grid_mapping_dict16.copy() # need shallow copy; update() returns None
grid_mapping_dict17.update({
    'geostationary': [
        (
            'latitude_of_projection_origin',
            'longitude_of_projection_origin',
            'perspective_point_height'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ],
    'oblique_mercator': [
        (
            'azimuth',
            'latitude_of_projection_origin',
            'longitude_of_projection_origin',
            'scale_factor_at_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ],
    'sinusoidal': [
        (
            'longitude_of_projection_origin'
        ),
        (
            'false_easting',
            'false_northing'
        ),
        (
            'projection_x_coordinate',
            'projection_y_coordinate'
        )
    ]
})

# horizontal datum names from https://github.com/cf-convention/cf-conventions/wiki/csv/horiz_datum.csv
horizontal_datum_names17 = {
 'Hungarian Datum 1909',
 'Taiwan Datum 1967',
 'Taiwan Datum 1997',
 'Iraqi Geospatial Reference System',
 'MGI 1901',
 'MOLDREF99',
 'Reseau Geodesique de la RDC 2005',
 'Serbian Reference Network 1998',
 'Red Geodesica de Canarias 1995',
 'Reseau Geodesique de Mayotte 2004',
 'Cadastre 1997',
 'Reseau Geodesique de Saint Pierre et Miquelon 2006',
 'Autonomous Regions of Portugal 2008',
 'Mexican Datum of 1993',
 'China 2000',
 'Sao Tome',
 'New Beijing',
 'Principe',
 'Reseau de Reference des Antilles Francaises 1991',
 'Tokyo 1892',
 'System Jednotne Trigonometricke Site Katastralni/05',
 'Sri Lanka Datum 1999',
 'System Jednotne Trigonometricke Site Katastralni/05 (Ferro)',
 'Geocentric Datum Brunei Darussalam 2009',
 'Turkish National Reference Frame',
 'Bhutan National Geodetic Datum',
 'Islands Net 2004',
 'International Terrestrial Reference Frame 2008',
 'Posiciones Geodesicas Argentinas 2007',
 'Marco Geodesico Nacional',
 'SIRGAS-Chile',
 'Costa Rica 2005',
 'Sistema Geodesico Nacional de Panama MACARIO SOLIS',
 'Peru96',
 'SIRGAS-ROU98',
 'SIRGAS_ES2007.8',
 'Ocotepeque 1935',
 'Sibun Gorge 1922',
 'Panama-Colon 1911',
 'Reseau Geodesique des Antilles Francaises 2009',
 'Corrego Alegre 1961',
 'South American Datum 1969(96)',
 'Papua New Guinea Geodetic Datum 1994',
 'Not specified (based on Airy 1830 ellipsoid)',
 'Not specified (based on Airy Modified 1849 ellipsoid)',
 'Not specified (based on Australian National Spheroid)',
 'Not specified (based on Bessel 1841 ellipsoid)',
 'Not specified (based on Bessel Modified ellipsoid)',
 'Not specified (based on Bessel Namibia ellipsoid)',
 'Not specified (based on Clarke 1858 ellipsoid)',
 'Not specified (based on Clarke 1866 ellipsoid)',
 'Not specified (based on Clarke 1866 Michigan ellipsoid)',
 'Not specified (based on Clarke 1880 (Benoit) ellipsoid)',
 'Not specified (based on Clarke 1880 (IGN) ellipsoid)',
 'Not specified (based on Clarke 1880 (RGS) ellipsoid)',
 'Not specified (based on Clarke 1880 (Arc) ellipsoid)',
 'Not specified (based on Clarke 1880 (SGA 1922) ellipsoid)',
 'Not specified (based on Everest 1830 (1937 Adjustment) ellipsoid)',
 'Not specified (based on Everest 1830 (1967 Definition) ellipsoid)',
 'Not specified (based on Everest 1830 Modified ellipsoid)',
 'Not specified (based on GRS 1980 ellipsoid)',
 'Not specified (based on Helmert 1906 ellipsoid)',
 'Not specified (based on Indonesian National Spheroid)',
 'Not specified (based on International 1924 ellipsoid)',
 'Not specified (based on Krassowsky 1940 ellipsoid)',
 'Not specified (based on NWL 9D ellipsoid)',
 'Not specified (based on Plessis 1817 ellipsoid)',
 'Not specified (based on Struve 1860 ellipsoid)',
 'Not specified (based on War Office ellipsoid)',
 'Not specified (based on WGS 84 ellipsoid)',
 'Not specified (based on GEM 10C ellipsoid)',
 'Not specified (based on OSU86F ellipsoid)',
 'Not specified (based on OSU91A ellipsoid)',
 'Not specified (based on Clarke 1880 ellipsoid)',
 'Not specified (based on Authalic Sphere)',
 'Not specified (based on GRS 1967 ellipsoid)',
 'Not specified (based on Average Terrestrial System 1977 ellipsoid)',
 'Not specified (based on Everest (1830 Definition) ellipsoid)',
 'Not specified (based on WGS 72 ellipsoid)',
 'Not specified (based on Everest 1830 (1962 Definition) ellipsoid)',
 'Not specified (based on Everest 1830 (1975 Definition) ellipsoid)',
 'Not specified (based on GRS 1980 Authalic Sphere)',
 'Not specified (based on Clarke 1866 Authalic Sphere)',
 'Not specified (based on International 1924 Authalic Sphere)',
 'Not specified (based on Hughes 1980 ellipsoid)',
 'Popular Visualisation Datum',
 'Greek',
 'Greek Geodetic Reference System 1987',
 'Average Terrestrial System 1977',
 'Kartastokoordinaattijarjestelma (1966)',
 'Rikets koordinatsystem 1990',
 'Samboja',
 'Lithuania 1994 (ETRS89)',
 'Tete',
 'Madzansua',
 'Observatario',
 'Moznet (ITRF94)',
 'Indian 1960',
 'Final Datum 1958',
 'Estonia 1992',
 'PDO Survey Datum 1993',
 'Old Hawaiian',
 'St. Lawrence Island',
 'St. Paul Island',
 'St. George Island',
 'Puerto Rico',
 'NAD83 Canadian Spatial Reference System',
 'Israel',
 'Locodjo 1965',
 'Abidjan 1987',
 'Kalianpur 1937',
 'Kalianpur 1962',
 'Kalianpur 1975',
 'Hanoi 1972',
 'Hartebeesthoek94',
 'CH1903',
 'CH1903+',
 'Swiss Terrestrial Reference Frame 1995',
 'NAD83 (High Accuracy Reference Network)',
 'Rassadiran',
 'European Datum 1950(1977)',
 'Dabola 1981',
 'System Jednotne Trigonometricke Site Katastralni',
 'Mount Dillon',
 'Naparima 1955',
 'European Libyan Datum 1979',
 'Chos Malal 1914',
 'Pampa del Castillo',
 'Korean Datum 1985',
 'Yemen National Geodetic Network 1996',
 'South Yemen',
 'Bissau',
 'Korean Datum 1995',
 'New Zealand Geodetic Datum 2000',
 'Accra',
 'American Samoa 1962',
 'Sistema de Referencia Geocentrico para America del Sur 1995',
 'Reseau Geodesique Francais 1993',
 'Posiciones Geodesicas Argentinas',
 'IRENET95',
 'Sierra Leone Colony 1924',
 'Sierra Leone 1968',
 'Australian Antarctic Datum 1998',
 'Pulkovo 1942(83)',
 'Pulkovo 1942(58)',
 'Estonia 1997',
 'Luxembourg 1930',
 'Azores Occidental Islands 1939',
 'Azores Central Islands 1948',
 'Azores Oriental Islands 1940',
 'Madeira 1936',
 'OSNI 1952',
 'Red Geodesica Venezolana',
 'Posiciones Geodesicas Argentinas 1998',
 'Albanian 1987',
 'Douala 1948',
 'Manoca 1962',
 'Qornoq 1927',
 'Scoresbysund 1952',
 'Ammassalik 1958',
 'Garoua',
 'Kousseri',
 'Egypt 1930',
 'Pulkovo 1995',
 'Adindan',
 'Australian Geodetic Datum 1966',
 'Australian Geodetic Datum 1984',
 'Ain el Abd 1970',
 'Afgooye',
 'Agadez',
 'Lisbon 1937',
 'Aratu',
 'Arc 1950',
 'Arc 1960',
 'Batavia',
 'Barbados 1938',
 'Beduaram',
 'Beijing 1954',
 'Reseau National Belge 1950',
 'Bermuda 1957',
 'Bogota 1975',
 'Bukit Rimpah',
 'Camacupa',
 'Campo Inchauspe',
 'Cape',
 'Carthage',
 'Chua',
 'Corrego Alegre 1970-72',
 "Cote d'Ivoire",
 'Deir ez Zor',
 'Douala',
 'Egypt 1907',
 'European Datum 1950',
 'European Datum 1987',
 'Fahud',
 'Gandajika 1970',
 'Garoua',
 'Guyane Francaise',
 'Hu Tzu Shan 1950',
 'Hungarian Datum 1972',
 'Indonesian Datum 1974',
 'Indian 1954',
 'Indian 1975',
 'Jamaica 1875',
 'Jamaica 1969',
 'Kalianpur 1880',
 'Kandawala',
 'Kertau 1968',
 'Kuwait Oil Company',
 'La Canoa',
 'Provisional South American Datum 1956',
 'Lake',
 'Leigon',
 'Liberia 1964',
 'Lome',
 'Luzon 1911',
 'Hito XVIII 1963',
 'Herat North',
 'Mahe 1971',
 'Makassar',
 'European Terrestrial Reference System 1989',
 'Malongo 1987',
 'Manoca',
 'Merchich',
 'Massawa',
 'Minna',
 'Mhast',
 'Monte Mario',
 "M'poraloko",
 'North American Datum 1927',
 'NAD27 Michigan',
 'North American Datum 1983',
 'Nahrwan 1967',
 'Naparima 1972',
 'New Zealand Geodetic Datum 1949',
 'NGO 1948',
 'Datum 73',
 'Nouvelle Triangulation Francaise',
 'NSWC 9Z-2',
 'OSGB 1936',
 'OSGB 1970 (SN)',
 'OS (SN) 1980',
 'Padang 1884',
 'Palestine 1923',
 'Congo 1960 Pointe Noire',
 'Geocentric Datum of Australia 1994',
 'Pulkovo 1942',
 'Qatar 1974',
 'Qatar 1948',
 'Qornoq',
 'Loma Quintana',
 'Amersfoort',
 'South American Datum 1969',
 'Sapper Hill 1943',
 'Schwarzeck',
 'Segora',
 'Serindung',
 'Sudan',
 'Tananarive 1925',
 'Timbalai 1948',
 'TM65',
 'Geodetic Datum of 1965',
 'Tokyo',
 'Trinidad 1903',
 'Trucial Coast 1948',
 'Voirol 1875',
 'Bern 1938',
 'Nord Sahara 1959',
 'Stockholm 1938',
 'Yacare',
 'Yoff',
 'Zanderij',
 'Militar-Geographische Institut',
 'Reseau National Belge 1972',
 'Deutsches Hauptdreiecksnetz',
 'Conakry 1905',
 'Dealul Piscului 1930',
 'Dealul Piscului 1970',
 'National Geodetic Network',
 'Kuwait Utility',
 'World Geodetic System 1972',
 'WGS 72 Transit Broadcast Ephemeris',
 'World Geodetic System 1984',
 'Anguilla 1957',
 'Antigua 1943',
 'Dominica 1945',
 'Grenada 1953',
 'Montserrat 1958',
 'St. Kitts 1955',
 'St. Lucia 1955',
 'St. Vincent 1945',
 'North American Datum 1927 (1976)',
 'North American Datum 1927 (CGQ77)',
 'Xian 1980',
 'Hong Kong 1980',
 'Japanese Geodetic Datum 2000',
 'Gunung Segara',
 'Qatar National Datum 1995',
 'Porto Santo 1936',
 'Selvagem Grande',
 'South American Datum 1969',
 'SWEREF99',
 'Point 58',
 'Fort Marigot',
 'Guadeloupe 1948',
 'Centre Spatial Guyanais 1967',
 'Reseau Geodesique Francais Guyane 1995',
 'Martinique 1938',
 'Reunion 1947',
 'Reseau Geodesique de la Reunion 1992',
 'Tahiti 52',
 'Tahaa 54',
 'IGN72 Nuku Hiva',
 'K0 1949',
 'Combani 1950',
 'IGN56 Lifou',
 'IGN72 Grande Terre',
 'ST87 Ouvea',
 'Petrels 1972',
 'Pointe Geologie Perroud 1950',
 'Saint Pierre et Miquelon 1950',
 'MOP78',
 'Reseau de Reference des Antilles Francaises 1991',
 'IGN53 Mare',
 'ST84 Ile des Pins',
 'ST71 Belep',
 'NEA74 Noumea',
 'Reseau Geodesique Nouvelle Caledonie 1991',
 'Grand Comoros',
 'International Terrestrial Reference Frame 1988',
 'International Terrestrial Reference Frame 1989',
 'International Terrestrial Reference Frame 1990',
 'International Terrestrial Reference Frame 1991',
 'International Terrestrial Reference Frame 1992',
 'International Terrestrial Reference Frame 1993',
 'International Terrestrial Reference Frame 1994',
 'International Terrestrial Reference Frame 1996',
 'International Terrestrial Reference Frame 1997',
 'International Terrestrial Reference Frame 2000',
 'Reykjavik 1900',
 'Hjorsey 1955',
 'Islands Net 1993',
 'Helle 1954',
 'Latvia 1992',
 'Porto Santo 1995',
 'Azores Oriental Islands 1995',
 'Azores Central Islands 1995',
 'Lisbon 1890',
 'Iraq-Kuwait Boundary Datum 1992',
 'European Datum 1979',
 'Istituto Geografico Militaire 1995',
 'Voirol 1879',
 'Chatham Islands Datum 1971',
 'Chatham Islands Datum 1979',
 'Sistema de Referencia Geocentrico para las AmericaS 2000',
 'Guam 1963',
 'Vientiane 1982',
 'Lao 1993',
 'Lao National Datum 1997',
 'Jouik 1961',
 'Nouakchott 1965',
 'Mauritania 1999',
 'Gulshan 303',
 'Philippine Reference System 1992',
 'Gan 1970',
 'Gandajika',
 'Marco Geocentrico Nacional de Referencia',
 'Reseau Geodesique de la Polynesie Francaise',
 'Fatu Iva 72',
 'IGN63 Hiva Oa',
 'Tahiti 79',
 'Moorea 87',
 'Maupiti 83',
 'Nakhl-e Ghanem',
 'Posiciones Geodesicas Argentinas 1994',
 'Katanga 1955',
 'Kasai 1953',
 'IGC 1962 Arc of the 6th Parallel South',
 'IGN 1962 Kerguelen',
 'Le Pouce 1934',
 'IGN Astro 1960',
 'Institut Geographique du Congo Belge 1955',
 'Mauritania 1999',
 'Missao Hidrografico Angola y Sao Tome 1951',
 'Mhast (onshore)',
 'Mhast (offshore)',
 'Egypt Gulf of Suez S-650 TL',
 'Tern Island 1961',
 'Cocos Islands 1965',
 'Iwo Jima 1945',
 'St. Helena 1971',
 'Marcus Island 1952',
 'Ascension Island 1958',
 'Ayabelle Lighthouse',
 'Bellevue',
 'Camp Area Astro',
 'Phoenix Islands 1966',
 'Cape Canaveral',
 'Solomon 1968',
 'Easter Island 1967',
 'Fiji Geodetic Datum 1986',
 'Fiji 1956',
 'South Georgia 1968',
 'Grand Cayman 1959',
 'Diego Garcia 1969',
 'Johnston Island 1961',
 'Little Cayman 1961',
 'Midway 1961',
 'Pico de las Nieves 1984',
 'Pitcairn 1967',
 'Santo 1965',
 'Viti Levu 1916',
 'Marshall Islands 1960',
 'Wake Island 1952',
 'Tristan 1968',
 'Kusaie 1951',
 'Deception Island',
 'Geocentric datum of Korea',
 'Hong Kong 1963',
 'Hong Kong 1963(67)',
 'Parametrop Zemp 1990',
 'Faroe Datum 1954',
 'Geodetic Datum of Malaysia 2000',
 'Karbala 1979',
 'Nahrwan 1934',
 'Rauenberg Datum/83',
 'Potsdam Datum/83',
 'Greenland 1996',
 'Vanua Levu 1915',
 'Reseau Geodesique de Nouvelle Caledonie 91-93',
 'ST87 Ouvea',
 'Kertau (RSO)',
 'Viti Levu 1912',
 'fk89',
 'Libyan Geodetic Datum 2006',
 'Datum Geodesi Nasional 1995',
 'Vietnam 2000',
 'SVY21',
 'Jamaica 2001',
 'NAD83 (National Spatial Reference System 2007)',
 'World Geodetic System 1966',
 'Croatian Terrestrial Reference System',
 'Bermuda 2000',
 'Pitcairn 2006',
 'Ross Sea Region Geodetic Datum 2000',
 'Slovenia Geodetic Datum 1996',
 'CH1903 (Bern)',
 'Bogota 1975 (Bogota)',
 'Lisbon 1937 (Lisbon)',
 'Makassar (Jakarta)',
 'Militar-Geographische Institut (Ferro)',
 'Monte Mario (Rome)',
 'Nouvelle Triangulation Francaise (Paris)',
 'Padang 1884 (Jakarta)',
 'Reseau National Belge 1950 (Brussels)',
 'Tananarive 1925 (Paris)',
 'Voirol 1875 (Paris)',
 'Batavia (Jakarta)',
 'Stockholm 1938 (Stockholm)',
 'Greek (Athens)',
 'Carthage (Paris)',
 'NGO 1948 (Oslo)',
 'System Jednotne Trigonometricke Site Katastralni (Ferro)',
 'Nord Sahara 1959 (Paris)',
 'Gunung Segara (Jakarta)',
 'Voirol 1879 (Paris)',
 'International Terrestrial Reference Frame 2005',
 'Ancienne Triangulation Francaise (Paris)',
 'Nord de Guerre (Paris)',
 'Madrid 1870 (Madrid)',
 'Lisbon 1890 (Lisbon)'}

# prime meridian_names from https://github.com/cf-convention/cf-conventions/wiki/csv/prime_meridian.csv
prime_meridian_names17 = {
 'Athens',
 'Bern',
 'Bogota',
 'Brussels',
 'Ferro',
 'Greenwich',
 'Jakarta',
 'Lisbon',
 'Madrid',
 'Oslo',
 'Paris',
 'Paris RGS',
 'Rome',
 'Stockholm'}


# ellipsoid names from https://github.com/cf-convention/cf-conventions/wiki/csv/ellipsoid.csv
ellipsoid_names17 = {
 'Airy 1830',
 'Airy Modified 1849',
 'Australian National Spheroid',
 'Average Terrestrial System 1977',
 'Bessel 1841',
 'Bessel Modified',
 'Bessel Namibia',
 'Bessel Namibia (GLM)',
 'CGCS2000',
 'Clarke 1858',
 'Clarke 1866',
 'Clarke 1866 Authalic Sphere',
 'Clarke 1866 Michigan',
 'Clarke 1880',
 'Clarke 1880 (Arc)',
 'Clarke 1880 (Benoit)',
 'Clarke 1880 (IGN)',
 'Clarke 1880 (RGS)',
 'Clarke 1880 (SGA 1922)',
 'Clarke 1880 (international foot)',
 'Danish 1876',
 'Everest (1830 Definition)',
 'Everest 1830 (1937 Adjustment)',
 'Everest 1830 (1962 Definition)',
 'Everest 1830 (1967 Definition)',
 'Everest 1830 (1975 Definition)',
 'Everest 1830 (RSO 1969)',
 'Everest 1830 Modified',
 'GEM 10C',
 'GRS 1967',
 'GRS 1967 Modified',
 'GRS 1980',
 'GRS 1980 Authalic Sphere',
 'Helmert 1906',
 'Hough 1960',
 'Hughes 1980',
 'IAG 1975',
 'Indonesian National Spheroid',
 'International 1924',
 'International 1924 Authalic Sphere',
 'Krassowsky 1940',
 'NWL 9D',
 'OSU86F',
 'OSU91A',
 'PZ-90',
 'Plessis 1817',
 'Popular Visualisation Sphere',
 'Sphere',
 'Struve 1860',
 'WGS 72',
 'WGS 84',
 'War Office'}

