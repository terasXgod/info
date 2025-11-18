def yaml_tokenizer(file_name: str) -> list:
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    result = []

    for line in lines:
        if line.strip() == '':
            continue
        
        stripped_line = line.lstrip()
        indent = len(line) - len(stripped_line)
        stripped_line = stripped_line.rstrip()
        if stripped_line[0] == '#':
            continue

        if stripped_line.startswith('- '):
            result.append(('DASH', '-', indent))
            rest = stripped_line[2:].strip()
            if rest and ':' in rest:
                key, value = rest.split(':', 1)
                key = key.strip().strip('\'\"')
                value = value.strip().strip('\'\"')
                result.append(('KEY', key, indent + 2))
                if value:
                    result.append(('VALUE', value, indent + 2))
        elif ':' in stripped_line:
            key, value = stripped_line.split(':', 1)
            key = key.strip().strip('\'\"')
            value = value.strip().strip('\'\"')
            result.append(('KEY', key, indent))
            if value:
                result.append(('VALUE', value, indent))
    
    return result


def yaml_parser(file_name: str):
    tokens = yaml_tokenizer(file_name)
    root = {}
    stack = [(-1, root, None)]

    i = 0
    while i < len(tokens):
        type_, val, indent = tokens[i]

        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()

        parent = stack[-1][1]
        parent_list_key = stack[-1][2]

        if type_ == "DASH":
            new_item = {}
            if isinstance(parent, dict) and parent_list_key is not None:
                if parent_list_key not in parent:
                    parent[parent_list_key] = []
                parent[parent_list_key].append(new_item)
            elif isinstance(parent, list):
                parent.append(new_item)
            stack.append((indent, new_item, None))
            i += 1
        
        elif type_ == "KEY":
            if i + 1 < len(tokens):
                next_type, next_val, next_indent = tokens[i + 1]
                if next_type == 'VALUE':
                    parent[val] = next_val
                    i += 2
                elif next_type == "DASH":
                    parent[val] = []
                    stack.append((indent, parent, val))
                    i += 1
                else:
                    cur_item = {}
                    parent[val] = cur_item
                    stack.append((next_indent, cur_item, None))
                    i += 1
            else:
                parent[val] = None
                i += 1
        
    return root