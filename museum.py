import requests
import logging


logging.basicConfig(filename='loggingfile.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class MuseumAPI:
    """
    MuseumAPI class to get response from API
    """
    def __init__(self):
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.base_url = "https://collectionapi.metmuseum.org/public/collection/v1/"

    def get_response(self, endpoint):
        """
        :param endpoint: API endpoint
        :return : response object
        """
        try:

            url = self.base_url+endpoint
            response = requests.get(url, headers=self.headers)

        except (requests.ConnectionError, requests.Timeout, requests.ConnectTimeout) as rerror:
            logging.error("Error occured : " + str(rerror))
        except requests.HTTPError as herror:
            logging.error("Error occured : " + str(herror))
        except Exception as e:
            logging.error("Error occured : " + str(e))

        return response

    def get_objectids(self):
        """
        It will get all object ids from museum API
        :return : It will return object ids in a dictionary
        :keys: * total: int
            count of object ids
                * object ids: list
            list of object ids
        """
        endpoint = "objects"
        return self.get_response(endpoint).json()

    def get_object_for_ids(self, object_id):
        """
        It will get an object with specified object ids
        :param object_id: object_id of the object
        :return : Dictionary containing objects
        """

<<<<<<< HEAD

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
=======
        endpoint = "objects/" + str(object_id)
        return self.get_response(endpoint).json()
>>>>>>> 61ef0a67c7aa08c2742faef21c1a4afdb3502b78
