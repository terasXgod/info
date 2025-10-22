# Author = Shageev Emir Salavatovich
# Group = P3132
# Date = 22.10.2025

import re

text = input()

gl = 'аеёиоуыэюяaeiouy'
sogl = 'бвгджзйклмньъпрстфхцчшщbcdfghjklmnpqrstvwxz'

regex = rf"\b[{sogl}]*([{gl}])(?:[{sogl}]|\1)*\b"

matches = [match.group(0) for match in re.finditer(regex, text, re.IGNORECASE)]
print("\n".join(sorted(matches, key = lambda x: (len(x), x))))