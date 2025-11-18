import yaml
from pprint import pprint
from time import time
from pytfvars import tfvars

def task2_solver(input_file_name: str ,output_file_name: str):
    with open(input_file_name, 'r', encoding='utf-8') as f:
        yaml_string = f.read()

    data = yaml.safe_load(yaml_string)
    hcl_string = tfvars.convert(data)

    with open(output_file_name, 'w', encoding='utf-8') as f:
        f.write(hcl_string)


if __name__ == "__main__":

    input_file_name = 'input.yml'
    output_file_name = 'output.tfvars'

    task2_solver(input_file_name, output_file_name)    

    # print(hcl_string)
    # pprint(data)
