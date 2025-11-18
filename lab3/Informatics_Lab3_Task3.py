# Author = Shageev Emir Salavatovich
# Group = P3132
# Date = 22.10.2025

import re

def passwordValidator(s: str):
    
    #rule1
    print('Rule 1', end=' ')
    rule1 = r"^.{5,}"
    if re.search(rule1, s):
        print(" [X] - Your password must be at least 5 characters.")
    else:
        print(" [ ] - Your password must be at least 5 characters.")

    #rule2
    print('Rule 2', end=' ')
    rule2 = r"\d"
    if re.search(rule2, s):
        print(" [X] - Your password must include a number.")
    else:
        print(" [ ] - Your password must include a number.")
    
    #rule3
    print('Rule 3', end=' ')
    rule3 = r"[A-Z]"
    if re.search(rule3, s):
        print(" [X] - Your password must include an uppercase letter.")
    else:
        print(" [ ] - Your password must include an uppercase letter.")

    #rule4
    print('Rule 4', end=' ')
    rule4 = r"[^a-z0-9]"
    if re.search(rule4, s, re.IGNORECASE):
        print(" [X] - Your password must include a special character.")
    else:
        print(" [ ] - Your password must include a special character.")

    #rule5
    print('Rule 5', end=' ')
    rule5 = r"\d"
    digits = re.findall(rule5, s)
    sumDigit = sum(map(int, digits))
    if sumDigit == 25:
        print(" [X] - The digits in your password must add up to 25.")
    else:
        print(" [ ] - The digits in your password must add up to 25.")

    #rule6
    print('Rule 6', end=' ')
    months = [
        "january", "february", "march", "april", "may", "june", 
        "july", "august", "september", "october", "november", "december"
    ]
    rule6 = r"|".join(months)
    if re.search(rule6, s, re.IGNORECASE):
        print(" [X] - Your password must include a month of the year.")
    else:
        print(" [ ] - Your password must include a month of the year.")

s = input('Enter your password: ')

passwordValidator(s)