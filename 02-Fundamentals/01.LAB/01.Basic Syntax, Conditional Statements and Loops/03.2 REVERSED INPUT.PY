text = input()

symbol = len(text) - 1

while symbol >= 0:
    print(text[symbol], end="")
    symbol -= 1