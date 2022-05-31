import re

text = input()

user = r'(^|(?<= ))(([a-z\d]+)([\.\-\_][a-z\d]+)?)'
host = r'@([a-z]+([\-\_][a-z]+)?\.[a-z]+(\.[a-z]+)?)'
pattern = user + host

emails = re.finditer(pattern, text)

for email in emails:
    print(email.group())
