from pprint import pprint
from yaml_parser import yaml_parser
from hcl_converter import hcl_converter, dict_to_hcl

def main_task_solver(input_file_name: str, output_file_name: str):
    parsed = yaml_parser(input_file_name)
    hcl_converter(parsed, output_file_name)

if __name__ == "__main__":

    input_file_name = "input.yml"
    output_file_name = "output.tf"

    main_task_solver(input_file_name, output_file_name)