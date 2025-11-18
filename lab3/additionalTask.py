import re
with open('main.css', 'r') as f:
    s = f.read()

# s = '.privet{\nkak:sdfsdf\ngg:you\n}'

mainSelector = r'\b\w+[ ]*\{[^}{]+}'
classSelector = r'\b\.\w+[ ]*\{[^}{]+}'
identySelector = r'\b\#\w+[ ]*\{[^}{]+}'
attributeSelector = r'\b\w+\[\w+\][ ]*\{[^}{]+}'
universalSelector = r'\b\*\w+\[\w+\][ ]*\{[^}{]+}'
psewdoSelector = r'\b\w+:\w+[ ]*\{[^}{]+}'

if input("хочешь искать основные селекторы? (y/n) ") == 'y':
    print(re.findall(mainSelector, s))
if input("хочешь искать селекторы классов? (y/n) ") == 'y':
    print(re.findall(classSelector, s))
if input("хочешь искать селекторы индентификаторов? (y/n)") == 'y':
    print(re.findall(identySelector, s))
if input("хочешь искать селекторы атрибутов? (y/n)") == 'y':
    print(re.findall(attributeSelector, s))
if input("хочешь искать универсальные атрибуты? (y/n)") == 'y':
    print(re.findall(universalSelector, s))
if input("хочешь искать псевдо-классы? (y/n)") == 'y':
    print(re.findall(psewdoSelector, s))
