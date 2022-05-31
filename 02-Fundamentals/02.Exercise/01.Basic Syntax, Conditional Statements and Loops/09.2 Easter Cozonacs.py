budget, flour_1kg = float(input()), float(input())

eggs_1pack, milk_1l = 0.75 * flour_1kg, 1.25 * flour_1kg
milk_250ml = milk_1l / 4

recipe = {
    'flour': flour_1kg,
    'eggs': eggs_1pack,
    'milk': milk_250ml,
}

cozonac = sum(recipe.values())
num_cozonacs, num_eggs = 0, 0

while True:
    if budget - cozonac < 0:
        break
    else:
        num_cozonacs += 1
        budget -= cozonac
        if num_cozonacs % 3 == 0:
            num_eggs -= num_cozonacs - 2
        num_eggs += 3

print(f'You made {num_cozonacs} cozonacs! Now you have {num_eggs} eggs and {budget:.2f}BGN left.')

