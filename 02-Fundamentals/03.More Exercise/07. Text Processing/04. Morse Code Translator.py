msg = input().split('|')
data = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '---': 'Ch',
    '-..': 'D',
    r'.': 'E',
    r'..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
}

res = str()
for element in msg:
    for symbol in element.split():
        res += data[symbol]
    res += ' '
print(res)
# [print(''.join([data[symbol] for symbol in element.split()]), end=' ') for element in msg]