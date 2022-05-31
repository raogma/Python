def append_to_dict(name_of_dict, dictionary, key, value):
    if key not in dictionary:
         dictionary[key] = value
    else:
        if name_of_dict == 'prices':
            dictionary[key] = value
        elif name_of_dict == 'quantities':
            dictionary[key] += value


prices = {}
quantities = {}

while True:
    command = input()
    if command == 'buy':
        break
    product, price, quantity = command.split(maxsplit=2)
    append_to_dict('prices', prices, product, float(price))
    append_to_dict('quantities', quantities, product, int(quantity))

[print(f"{product} -> {prices[product] * quantities[product]:.2f}") for product in prices]