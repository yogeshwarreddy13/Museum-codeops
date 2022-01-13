import unittest
import logging
import os
import json
from unittest.mock import patch
from Museum_API.museum import MuseumAPI

logging.basicConfig(filename='logging_statements.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class TestMuseumApi(unittest.TestCase):

    def setUp(self):
        self.endpoint = "objects"

    def test_api_url(self):
        museum_url = MuseumAPI()
        self.assertEqual(museum_url.get_response(self.endpoint).status_code, 200)

    def test_object_url(self):
        """checks for the status code from the actual url"""
        museum_url = MuseumAPI()
        self.assertEqual(museum_url.get_response(self.endpoint+'y').status_code, 404)

    @patch('Museum_API.museum.requests.get')
    def test_to_get_response_ok(self, mock_get):
        """get ok response from the mocked url"""
        museum_url = MuseumAPI()

        # Configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = True

        response = museum_url.get_object_ids()

        self.assertIsNotNone(response)

    def test_get_object_id(self):
        """assert the mocked data generated after calling original
            function with the truth file"""
        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'actual_data/objectids.json'), encoding='utf-8') as file_name:
                json_data = json.load(file_name)
                with patch('Museum_API.museum.requests.get') as mock_get:
                    mock_get.return_value.json.return_value = json_data
                    sample = MuseumAPI()
                    resp = sample.get_object_ids()

                    self.assertEqual(resp, json_data)
        except FileNotFoundError as file_err:
            logging.exception('check for correct path because %s', file_err)

    def test_get_object_for_id(self):
        """assert the mocked data generated after calling original
            function with the truth file"""
        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'actual_data/objdata.json'), encoding='utf-8') as file_name:
                json_data = json.load(file_name)
                with patch('Museum_API.museum.requests.get') as mock_get:
                    mock_get.return_value.json.return_value = json_data
                    sample = MuseumAPI()
                    resp = sample.get_object_for_ids('1')

                    self.assertEqual(resp, json_data)
        except FileNotFoundError as file_err:
            logging.exception('check for correct path because %s', file_err)


if __name__ == '__main__':
    unittest.main()