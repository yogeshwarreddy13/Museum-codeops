from Museum_API.museum import MuseumAPI
from Museum_API.converters import Converter, flatten
import logging
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(filename="logging_file.log", level=logging.ERROR,
                    format="%(asctime)s:%(levelname)s:%(message)s")

museum = MuseumAPI()
try:
    # getting object_ids from museum API
    object_ids = museum.get_object_ids()["objectIDs"][0: 50]

    keys = ("constituents", "measurements", "tags")
    # getting objects with specified object_id
    object_list = list(map(lambda object_id: flatten(museum.get_object_for_ids(object_id), keys),
                           object_ids))
except Exception as e:
    logging.error("error occurred : " + str(e))


files_dir = os.path.join(base_dir, "files/")
# field names from object_list
field_names = object_list[0].keys()


try:
    Converter.convert_to_csv(object_list, field_names, os.path.join(files_dir, "museum_csv.csv"))
    Converter.convert_to_pdf(object_list, os.path.join(files_dir, "museum_pdf.pdf"))
    Converter.convert_to_html(object_list, os.path.join(files_dir, "museum_html.html"))
    Converter.convert_to_xml(object_list, os.path.join(files_dir, "museum_xml.xml"))
    Converter.convert_to_excel(object_list, os.path.join(files_dir, "museum_excel.xlsx"))
except Exception as e:
    logging.error("error occurred : " + str(e))
