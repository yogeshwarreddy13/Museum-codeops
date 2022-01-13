from Museum_API.museum import MuseumAPI
from Museum_API.converters import Converter, flatten
import json
import os

museum = MuseumAPI()

#object_ids = museum.get_object_ids()

#with open('data.json', 'w') as outfile:
#    json.dump(object_ids, outfile)




# getting objects with specified object_id

#object_list = museum.get_object_for_ids('1')

#with open('objdata.json', 'w') as outfile:
#    json.dump(object_list, outfile)

#object_ids = museum.get_object_ids()["objectIDs"][0: 50]

#keys = ("constituents", "measurements", "tags")
# getting objects with specified object_id
#object_list = list(map(lambda object_id: flatten(museum.get_object_for_ids(object_id), keys),
#                       object_ids))

#print(object_list)

with open('C:/Users/yogeshwar/PycharmProjects/Museum API/tests/temp_data/objects_list_for_conversion.json', encoding='utf-8') as file_ptr:
    data = json.load(file_ptr)

#Converter.convert_to_csv(data, "museum_data.csv")

Converter.convert_to_pdf(data, "museum_data.pdf")