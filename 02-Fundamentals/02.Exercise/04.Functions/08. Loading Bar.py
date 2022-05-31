def loading(number):
    number /= 10
    bar_list = ["."] * 10
    bar = ""
    for i in range(len(bar_list)):
        number -= 1
        if number >= 0:
            bar_list[i] = "%"
    for element in bar_list:
        bar += element
    return f"[{bar}]"


number_input = int(input())
if number_input < 100:
    print(f"{number_input}% {loading(number_input)}")
    print("Still loading...")
else:
    print(f"{number_input}% Complete!")
    print(loading(number_input))
