import sys
import pandas as pd
import logging
import unittest
import os
import json

from Museum_API.converters import Converter

logging.basicConfig(filename='test_logging.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class TestConverter(unittest.TestCase):
    """
    Class to test the functionality of all the functions of Converter
    class.
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        function to load temporary data in a member variable for testing.
        """
        cls.data = None # list of dicts to be converted to different formats
        cls.temp_data_dir = 'C:\\Users\\yogeshwar\\PycharmProjects\\Museum API\\tests\\'
        cls.maxDiff = None

        try:
            with open('temp_data/objects_list_for_conversion.json', encoding='utf-8') as file:
                cls.data = json.load(file)

        except FileNotFoundError as fe:
            logging.error('File not found : %s', fe.args[-1])
            sys.exit(1)

    def test_convert_to_csv(self):
        """
        function to test functionality of converting given data
        to csv file.
        """
        new_csv_file_name = 'museum_data.csv'
        new_csv_file_path = os.path.join(self.temp_data_dir, 'temp_data\\museum_data.csv')
        Converter.convert_to_csv(self.data, new_csv_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'actual_data\\museum_data.csv'), 'r', encoding='utf-8') \
                    as old_csv, \
                    open(new_csv_file_path, 'r', encoding='utf-8') as newly_converted_csv:
                self.assertEqual(old_csv.read(), newly_converted_csv.read())

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

    def test_convert_to_csv_when_object_list_is_invalid(self):
        """
        test failure of convert_to_csv function when object_list
        argument is invalid.
        """
        new_csv_file_name = 'museum_data.csv'
        new_csv_file_path = os.path.join(self.temp_data_dir, new_csv_file_name)
        object_list = None
        with self.assertRaises(TypeError):
            Converter.convert_to_csv(object_list, new_csv_file_path)

    def test_convert_to_pdf(self):
        """
        function to test functionality of converting given data
        to csv file.
        """
        new_pdf_file_name = 'museum_data.pdf'
        new_pdf_file_path = os.path.join(self.temp_data_dir, 'temp_data\\museum_data.pdf')
        Converter.convert_to_pdf(self.data, new_pdf_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'actual_data\\museum_data.pdf'), 'rb') \
                    as old_pdf, \
                    open(new_pdf_file_path, 'rb') as newly_converted_pdf:
                self.assertNotEqual(old_pdf.read(), newly_converted_pdf.read())

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

    def test_convert_to_pdf_when_object_list_is_invalid(self):
        """
        test failure of convert_to_pdf function when object_list
        argument is invalid.
        """
        new_pdf_file_name = 'museum_data.pdf'
        new_pdf_file_path = os.path.join(self.temp_data_dir, new_pdf_file_name)
        object_list = None
        with self.assertRaises(TypeError):
            Converter.convert_to_pdf(object_list, new_pdf_file_path)

    def test_convert_to_html(self):
        """
        function to test functionality of converting given data
        to html file.
        """
        new_html_file_name = 'museum_data.html'
        new_html_file_path = os.path.join(self.temp_data_dir, 'temp_data\\museum_data.html')
        Converter.convert_to_html(self.data, new_html_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'actual_data\\museum_data.html'), 'r', encoding='utf-8') \
                    as old_html, \
                    open(new_html_file_path, 'r', encoding='utf-8') as newly_converted_html:
                self.assertEqual(old_html.read(), newly_converted_html.read())

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

    def test_convert_to_html_when_object_list_is_invalid(self):
        """
        test failure of convert_to_html function when object_list
        argument is invalid.
        """
        new_html_file_name = 'museum_data.html'
        new_html_file_path = os.path.join(self.temp_data_dir, new_html_file_name)
        object_list = None
        with self.assertRaises(TypeError):
            Converter.convert_to_html(object_list, new_html_file_path)

    def test_convert_to_xml(self):
        """
        function to test functionality of converting given data
        to xml file.
        """
        new_xml_file_name = 'museum_data.html'
        new_xml_file_path = os.path.join(self.temp_data_dir, 'temp_data\\museum_data.xml')
        Converter.convert_to_xml(self.data, new_xml_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'actual_data\\museum_data.xml'), 'r', encoding='utf-8') \
                    as old_xml, \
                    open(new_xml_file_path, 'r', encoding='utf-8') as newly_converted_xml:
                self.assertEqual(old_xml.read(), newly_converted_xml.read())

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

    def test_convert_to_xml_when_object_list_is_invalid(self):
        """
        test failure of convert_to_xml function when object_list
        argument is invalid.
        """
        new_xml_file_name = 'museum_data.xml'
        new_xml_file_path = os.path.join(self.temp_data_dir, new_xml_file_name)
        object_list = None
        with self.assertRaises(TypeError):
            Converter.convert_to_xml(object_list, new_xml_file_path)

    def test_convert_to_excel(self):
        """
        function to test functionality of converting given data
        to excel file.
        """
        new_excel_file_name = 'museum_data.xlsx'
        new_excel_file_path = os.path.join(self.temp_data_dir, 'temp_data\\museum_data.xlsx')
        Converter.convert_to_excel(self.data, new_excel_file_path)

        actual_excel_df = pd.read_excel(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                       'actual_data\\museum_data.xlsx'))
        temp_excel_df = pd.read_excel(new_excel_file_path)

        temp_excel_df.compare(actual_excel_df)

    def test_convert_to_excel_when_object_list_is_invalid(self):
        """
        test failure of convert_to_excel function when object_list
        argument is invalid.
        """
        new_excel_file_name = 'museum_data.xlsx'
        new_excel_file_path = os.path.join(self.temp_data_dir, new_excel_file_name)
        object_list = None
        with self.assertRaises(TypeError):
            Converter.convert_to_xml(object_list, new_excel_file_path)


if __name__ == '__main__':
    unittest.main()