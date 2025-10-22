# Author = Shageev Emir Salavatovich
# Group = P3132
# Date = 22.10.2025

import re

regex = r"\b(\w+)(\s+\1)+\b"

text = input()

# matches = [match.group(0) for match in re.finditer(regex, text, re.IGNORECASE)]
# print(f"Найденные повторы: {matches}")

fixed_text = re.sub(regex, r"\1", text, flags=re.IGNORECASE)

print(fixed_text)
