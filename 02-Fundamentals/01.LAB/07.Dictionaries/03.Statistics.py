bakery = {}
while True:
    command = input()
    if command == 'statistics':
        break

    tokens = command.split(': ')
    product = tokens[0]
    quantity = int(tokens[1])
    if product not in bakery:
        bakery[product] = quantity
        continue
    bakery[product] += quantity

print("Products in stock:")

[print(f'- {product}: {quantity}') for product, quantity in bakery.items()]
print(f'Total Products: {len(bakery.keys())}')
print(f'Total Quantity: {sum(bakery.values())}')
