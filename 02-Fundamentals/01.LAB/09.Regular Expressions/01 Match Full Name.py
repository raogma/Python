from re import findall

regex_line = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
text = input()
print(' '.join(findall(regex_line, text)))
