strawberries_price = float(input())

bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - 0.4 * raspberries_price
bananas_price = raspberries_price - 0.8 * raspberries_price

total_price = strawberries_quantity * strawberries_price + bananas_price * bananas_quantity + oranges_price * oranges_quantity + raspberries_quantity * raspberries_price

print(total_price)