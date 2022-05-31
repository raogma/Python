products = input().split()
searched = input().split()

products_dict = {products[i]: int(products[i + 1]) for i in range(0, len(products), 2)}

for item in searched:
    if item in products_dict:
        print(f"We have {products_dict[item]} of {item} left")
        continue
    print(f"Sorry, we don't have {item}")