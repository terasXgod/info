from pprint import pprint
from yaml_parser import yaml_parser
from xml_converter import xml_converter

input_file_name = "input.yml"
output_file_name = "output.xml"

parsed = yaml_parser(input_file_name)

pprint(parsed)

xml_converter(parsed, output_file_name)