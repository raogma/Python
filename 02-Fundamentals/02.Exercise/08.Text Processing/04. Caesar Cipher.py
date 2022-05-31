txt = input()
encrypted_txt = str()

for i in range(len(txt)):
    encrypted_txt += chr(ord(txt[i]) + 3)

print(encrypted_txt)