num_of_bottles = int(input()) #750ml
bottle = 750
total_mls = num_of_bottles * bottle
dishes = 5
num_of_dishes = 0
pots = 15
num_of_pots = 0
command = input()
counter = 0

while command != "End":
    number = int(command)
    counter += 1
    if counter % 3 == 0:
        num_of_pots += number
        total_mls -= number * pots
    else:
        num_of_dishes += number
        total_mls -= number * dishes
    if total_mls < 0:
        print(f"Not enough detergent, {abs(total_mls)} ml. more necessary!")
        break
    command = input()
else:
    print("Detergent was enough!")
    print(f"{num_of_dishes} dishes and {num_of_pots} pots were washed.")
    print(f"Leftover detergent {total_mls} ml.")
