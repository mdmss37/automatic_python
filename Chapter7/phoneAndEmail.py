    #! python3
# phoneAndEmail.py
# - Finds phone numbers and email adress from the clipboard.

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separation
    (\d{3}) # first 3 digit
    (\s|-|\.) # separation
    (\d{4}) # first 4 digit
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extention
    )''', re.VERBOSE)

# Creates email Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @                 # @ symbol
    [a-zA-Z0-9.-]+    # domain name
    (\.[a-zA-Z]{2,4}) # .something
    )''', re.VERBOSE)

# Find matches in clipboard
text = pyperclip.paste().encode('utf-8')
print(type(text))
matches = []
for groups in phoneRegex.findall(text):
    phonenum = "-".join([groups[1],groups[3],groups[5]])
    if groups[8] != "":
        phonenum += " x " + groups[8]
    matches.append(phonenum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy result to the clipboard
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to the clipboard: ")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses were found.")











