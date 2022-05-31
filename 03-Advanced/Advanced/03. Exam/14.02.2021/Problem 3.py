def stock_availability(inventory: list, option: str, *args):
    if option == 'delivery':
        for element in args:
            inventory.append(element)
    elif option == 'sell':
        if not args:
            if inventory:
                inventory.pop(0)
        for x in args:
            if isinstance(x, int):
                for _ in range(x):
                    if inventory:
                        inventory.pop(0)
            else:
                if x in inventory:
                    inventory = [i for i in inventory if i != x]
    return inventory


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))