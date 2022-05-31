command = input()

counter_c = 0
counter_o = 0
counter_n = 0
word = ""

while command != "End":
    if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:   #A-Z; a-z
        if ord(command) == 99:
            counter_c += 1
            if counter_c > 1:
                word += command

        elif ord(command) == 111:
            counter_o += 1
            if counter_o > 1:
                word += command

        elif ord(command) == 110:
            counter_n += 1
            if counter_n > 1:
                word += command

        else:
            word += command
    if counter_c >= 1 and counter_o >= 1 and counter_n >= 1:
        print(f"{word}", end=" ")
        word = ""
        counter_c = 0
        counter_o = 0
        counter_n = 0
    command = input()