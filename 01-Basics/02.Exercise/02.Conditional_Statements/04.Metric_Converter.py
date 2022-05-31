num = float(input())
input_text = input()
output_text = input()

if input_text == "mm":
    if output_text == "cm":
        num_v2 = num / 10
        print(f"{num_v2:.3f}")
    elif output_text == "m":
        num_v2 = num / 1000
        print(f"{num_v2:.3f}")

elif input_text == "cm":
    if output_text == "mm":
        num_v2 = num * 10
        print(f"{num_v2:.3f}")
    elif output_text == "m":
        num_v2 = num / 100
        print(f"{num_v2:.3f}")

elif input_text == "m":
    if output_text == "cm":
        num_v2 = num * 100
        print(f"{num_v2:.3f}")
    elif output_text == "mm":
        num_v2 = num * 1000
        print(f"{num_v2:.3f}")
