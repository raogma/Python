from re import finditer

regex = r'(?P<day>\d{2})(?P<separator>[/\.-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b'
dates = finditer(regex, input())

for date in dates:
    print(f'Day: {date.groupdict()["day"]}, Month: {date.groupdict()["month"]}, Year: {date.groupdict()["year"]}')