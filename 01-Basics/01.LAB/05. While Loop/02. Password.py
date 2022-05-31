username = input()
correct_pass = input()

input_pass = input()

while input_pass != correct_pass:
    input_pass = input()

else:
    print(f"Welcome {username}!")
