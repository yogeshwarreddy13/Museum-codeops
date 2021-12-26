from museum import MuseumAPI
from converters import Converter, flatten
import logging
import sys

logging.basicConfig(filename='loggingfile.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

museum = MuseumAPI()

try:
    # getting objectids from museum API
    object_ids = museum.get_objectids()['objectIDs'][0: 50]

    keys = ('constituents', 'measurements', 'tags')
    # getting objects with specified objectid
    object_list = list(map(lambda object_id: flatten(museum.get_object_for_ids(object_id), keys), object_ids))
except Exception as e:
    logging.error("error occured : " + str(e))
    sys.exit(1)

# field names from objectlist
field_names = object_list[0].keys()

converters = Converter(object_list)
try:
    converters.convert_to_csv(field_names)
    converters.convert_to_pdf()
    converters.convert_to_html()
    converters.convert_to_xml()
    converters.convert_to_excel()
except Exception as e:
    logging.error("error occured : " + str(e))
