start = input() #97
end = input()   #122
skip = input()

counter = 0

for letter1 in range(ord(start), ord(end) + 1):
    if chr(letter1) != skip:
        for letter2 in range(ord(start), ord(end) + 1):
            if chr(letter2) != skip:
                for letter3 in range(ord(start), ord(end) + 1):
                    if chr(letter3) != skip:
                        counter += 1
                        print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}", end=" ")
print(counter)
