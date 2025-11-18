def dict_to_xml(d: dict, indent: int = 0) -> str:
    xml = ''
    space = '  ' * indent
    for key, value in d.items():
        if isinstance(value, dict):
            xml += f'{space}<{key}> \n'
            xml += dict_to_xml(value, indent + 1)
            xml += f'{space}</{key}>\n'
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    xml += f'{space}- <{key}> \n'
                    xml += dict_to_xml(item, indent + 1)
                    xml += f'{space}</{key}>\n'
                else:
                    xml += f'{space}<{key}>["{item}"]</{key}>\n'
        else:
            xml += f'{space}<{key}>"{value}"</{key}>\n'
    return xml

def xml_converter(d: dict, file_output: str):
    with open(file_output, 'w', encoding='utf-8') as f:
        f.write(dict_to_xml(d))