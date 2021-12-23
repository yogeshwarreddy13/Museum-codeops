import requests
import csv
import pandas as pd
import pdfkit
import logging
import os

logging.basicConfig(filename='loggingfile.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def get_response(endpoint):
    try:
        base_url = "https://collectionapi.metmuseum.org/public/collection/v1/"
        url = base_url+endpoint
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
    except (requests.ConnectionError, requests.Timeout, requests.ConnectTimeout) as rerror:
        logging.error("Error occured : " + str(rerror))
    except requests.HTTPError as herror:
        logging.error("Error occured : " + str(herror))
    except Exception as e:
        logging.error("Error occured : " + str(e))

    return response


def get_objectids():

    endpoint = "objects"
    return get_response(endpoint).json()


def get_object_for_ids(object_id):

    endpoint = "objects/" + str(object_id)
    return get_response(endpoint).json()


def flatten(obj, keys):
    """
     It will flatten the dictionary object specified in the argument
     obj: object to be flattened
     keys: list of keys which are not flattened by default
     return: reference of flattened object
    """
    for key in keys:
        values = obj[key]
        if values:
            for value in values:
                for k, v in value.items():
                    obj[k] = v
            del obj[key]
    return obj


object_ids = get_objectids()['objectIDs'][0: 50]

keys = ('constituents', 'measurements', 'tags')

object_list = list(map(lambda object_id: flatten(get_object_for_ids(object_id), keys), object_ids))
field_names = object_list[0].keys()


def convert_to_csv(objectlist, fnames):
    try:
        with open("mymuseum.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fnames)
            writer.writeheader()
            for obj in objectlist:
                d = {key: value for key, value in obj.items() if key in fnames}
                writer.writerow(d)
    except PermissionError as pe:
        logging.error('Error occured in convert_to_csv func : ' + str(pe))
    except FileNotFoundError as fe:
        logging.error('error occured in convert_to_csv func : ' + str(fe))
    except Exception as e:
        logging.error("Error occured : " + str(e))


def convert_to_pdf(objectlist):
    try:
        df = pd.DataFrame(data=objectlist)
        temp_html_filename = 'temp.html'
        df.to_html(temp_html_filename)
        pdfkit.from_file(temp_html_filename, output_path="mymuseum.pdf",
                         options={'page-height': '1500', 'page-width': '660'})
        os.remove(temp_html_filename)
    except PermissionError as pe:
        logging.error('Error occured in convert_to_pdf func : ' + str(pe))
    except FileNotFoundError as fe:
        logging.error('Error occcured in convert_to_pdf func : ' + str(fe))
    except Exception as e:
        logging.error("Error occured : " + str(e))


def convert_to_html(objectlist):
    try:
        df = pd.DataFrame(data=objectlist)
        df.to_html("myhtml.html")
    except PermissionError as pe:
        logging.error('Error occured in convert_to_html func : ' + str(pe))
    except FileNotFoundError as fe:
        logging.error('Error occcured in convert_to_html func : ' + str(fe))
    except Exception as e:
        logging.error("Error occured : " + str(e))


def convert_to_xml(objectlist):
    try:
        df = pd.DataFrame(data=objectlist)
        df.to_xml("myxml.xml")
    except PermissionError as pe:
        logging.error('Error occured in convert_to_xml func : ' + str(pe))
    except FileNotFoundError as fe:
        logging.error('Error occcured in convert_to_xml func : ' + str(fe))
    except Exception as e:
        logging.error("Error occured : " + str(e))


def convert_to_excel(objectlist):
    try:
        df = pd.DataFrame(data=objectlist)
        df.to_excel("myexcel.excel")
    except PermissionError as pe:
        logging.error('Error occured in convert_to_excel func : ' + str(pe))
    except FileNotFoundError as fe:
        logging.error('Error occured in convert_to_excel func : ' + str(fe))
    except Exception as e:
        logging.error("Error occured : " + str(e))


convert_to_csv(object_list, field_names)
convert_to_pdf(object_list)
convert_to_html(object_list)
convert_to_xml(object_list)
convert_to_excel(object_list)

#commit