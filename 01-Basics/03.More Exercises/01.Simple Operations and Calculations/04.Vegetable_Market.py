price_1kg_veggies = float(input())
price_1kg_fruits = float(input())
total_kgs_veggies = float(input())
total_kgs_fruits = float(input())

total_price_lv = price_1kg_veggies * total_kgs_veggies + price_1kg_fruits * total_kgs_fruits
total_price_eu = total_price_lv / 1.94

print(f"{total_price_eu:.2f}")