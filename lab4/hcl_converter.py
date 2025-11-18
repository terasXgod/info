def dict_to_hcl(d: dict, indent: int = 0) -> str:
    
    hcl = ''
    space = '  ' * indent
    for key, value in d.items():
        if isinstance(value, dict):
            hcl += f'{space}{key} {{\n'
            hcl += dict_to_hcl(value, indent + 1)
            hcl += f'{space}}}\n'
        elif isinstance(value, list):
            hcl += f'{space}{key} = [\n'
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    hcl += f'{space+"  {"}\n'
                    hcl += dict_to_hcl(item, indent + 2)
                    if i != len(value) - 1:
                        hcl += f'{space+"  },"}\n'
                    else:
                        hcl += f'{space+"  }"}\n'
                else:
                    hcl += f'{space}{key} = ["{item}"]\n'
            hcl += f"{space}]\n"
        else:
            hcl += f'{space}{key} = "{value}"\n'
    return hcl

def hcl_converter(d: dict, file_output: str):
    with open(file_output, 'w', encoding='utf-8') as f:
        f.write(dict_to_hcl(d))