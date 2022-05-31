command = input()

kids = 0
adults = 0
price_kids = 5
price_adults = 15

while command != "Christmas":
    age = int(command)
    if age <= 16:
        kids += 1
    else:
        adults += 1
    command = input()

toys = kids * price_kids
pullovers = adults * price_adults

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys}")
print(f"Money for sweaters: {pullovers}")
