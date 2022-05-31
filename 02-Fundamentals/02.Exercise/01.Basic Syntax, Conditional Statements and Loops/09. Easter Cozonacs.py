budget = float(input())
one_kg_flour = float(input())

one_pack_eggs = 0.75 * one_kg_flour
one_ltr_milk = 1.25 * one_kg_flour
quarter_ltr_milk = one_ltr_milk / 4

price_per_cozonac = one_kg_flour + one_pack_eggs + quarter_ltr_milk
cozonacs_counter = 0
eggs_counter = 0

while budget >= price_per_cozonac:
    budget -= price_per_cozonac
    cozonacs_counter += 1
    eggs_counter += 3
    if cozonacs_counter % 3 == 0:
        lost_eggs = cozonacs_counter - 2
        eggs_counter -= lost_eggs

print(f"You made {cozonacs_counter} cozonacs! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")
