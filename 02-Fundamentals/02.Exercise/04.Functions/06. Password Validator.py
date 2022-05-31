def pass_validator(password):
    digit_counter = 0
    is_long = False
    has_letts = False
    has_nums = False
    is_2_nums = False

    if 6 <= len(password) <= 10:
        is_long = True
    for symbol in password:
        if 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122 or 48 <= ord(symbol) <= 57:
            if 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122:
                has_letts = True
            if 48 <= ord(symbol) <= 57:
                has_nums = True
                digit_counter += 1
                if digit_counter >= 2:
                    is_2_nums = True
        else:
            has_letts = False
            has_nums = False
            break

    if is_long and has_letts and has_nums and is_2_nums:
        print("Password is valid")
    if not is_long:
        print("Password must be between 6 and 10 characters")
    if not has_letts or not has_nums:
        print("Password must consist only of letters and digits")
    if not is_2_nums:
        print("Password must have at least 2 digits")


password_input = input()
(pass_validator(password_input))
