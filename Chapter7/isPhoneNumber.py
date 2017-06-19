# https://forum.sublimetext.com/t/how-do-i-setup-python3-3-and-sublime-text-2-correctly-osx/7811

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office. "
for i in range(0,len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number is found: " + chunk)
print("Done")

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("My number is 415-555-4242.")
print("Phone number is found: " + mo.group())

# Using group to store match
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 415-555-4242.")
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group())

areaCode, mainNumber = mo.groups()
print("areacode: " + areaCode)
print("mainnunbmer: " + mainNumber)

# Escape parenthesis
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My phone number is (415) 512-4232.")
print(mo.group(1))
print(mo.group(2))

# Matching multipul group with pipe
hereRegex = re.compile(r'Batman|Tina Fey')
mo1 = hereRegex.search("Batman and Tina Fey")
print(mo1.group())
mo2 = hereRegex.search("Tina Fey and Batman")
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search("Batmobile lost a wheel.")
print(mo.group())
print(mo.group(1))

# Optional matching with question mark

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())
print(mo1.group(1))

mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())
print(mo2.group(1))

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.search("My number is 415-321-4536")
print(mo1.group())
mo2 = phoneNumRegex.search("My number is 321-4536")
print(mo2.group())

# Matching zero or more with star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())
mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())
mo3 = batRegex.search("The Adventures of Batwowowoman")
print(mo3.group())

# Matching one or more with plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search("The Adventures of Batman")
print(mo1 == None)
mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())
mo3 = batRegex.search("The Adventures of Batwowowoman")
print(mo3.group())

# Matching specific number of repetitions with {}
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search("HaHaHa")
print(mo1.group())
print(mo1.group(1))

mo2 = haRegex.search("Ha")
print(mo2)

# greedy and non greedy matching
greedyhaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyhaRegex.search("HaHaHaHaHa")
print(mo1.group())

NongreedyhaRegex = re.compile(r'(Ha){3,5}?')
mo1 = NongreedyhaRegex.search("HaHaHaHaHa")
print(mo1.group())

# findall

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("Cell: 415-555-9999 Work: 212-555-0000")
print(mo.group())
mo = phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo)

# character classes
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(' 12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall(' RoboCop eats baby food. BABY FOOD.')
print(mo)

consonantRegex = re.compile(r'[^aeiouAEIOU ]')
mo = consonantRegex.findall(' RoboCop eats baby food. BABY FOOD.')
print(mo)

# the carat and dollar sign characters
beginswithhello = re.compile(r'^Hello')
mo = beginswithhello.search("Hello world!")
print(mo)
mo = beginswithhello.search("He said Hello.")
print(mo)

endswithnumber = re.compile(r'\d+$')
mo = endswithnumber.search("your number is 42")
print(mo.group())
mo = endswithnumber.search("42 is your number")
print(mo)

wholestringisnum = re.compile(r'^\d+$')
mo = wholestringisnum.search("0123456789")
print(mo)
mo = wholestringisnum.search("01234xvb56789")
print(mo)
mo = wholestringisnum.search("01234 56789")
print(mo)

# wildcard character
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# matching everything with dot star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search(' First Name: Al Last Name: Sweigart')
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search(' < To serve man > for dinner. >')
print(mo)

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search(' < To serve man > for dinner. >')
print(mo)

# mathing newline with dot character
noNewlineRegex = re.compile(r'.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.'). group())
NewlineRegex = re.compile(r'.*', re.DOTALL)
print(NewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.'). group())

# case insensitive matching
robocop = re.compile(r'robocop', re.IGNORECASE) #or re.I

print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

# substituting string with sub() method
nameRegex = re.compile(r'Agent \w+')
print(nameRegex.sub("CENSORED", 'Agent Alice gave the secret documents to Agent Bob.'))

agentNamesRegex = re.compile(r'Agent (\w)?\w*')
print(agentNamesRegex.findall('Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

# managing complex regex
phoneNumRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? #areaCode
    (\s|-|\.)? #separator
    \d{3} # first 3 digits
    (\s|-|\.)? #separator
    \d{4} #last 4 digits
    \s*(ext|x|ext.)? #extention prefix
    \s*(\d{2,5})? #extention num
    )''', re.VERBOSE)

mo = phoneNumRegex.search("My phone number is (415) 512-4232 999.")
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group(6))


















