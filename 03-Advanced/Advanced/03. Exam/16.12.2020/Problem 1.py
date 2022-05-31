males = [x for x in list(map(int, input().split())) if x > 0]
females = [x for x in list(map(int, input().split())) if x > 0]

matches = 0

while len(males) > 0 and len(females) > 0:
    male, female = males.pop(), females.pop(0)
    if male == female:
        matches += 1
        continue
    else:
        # special
        if male % 25 == 0 or female % 25 == 0:
            if male % 25 == 0:
                males.pop()
                females.insert(0, female)
                continue
            else:
                females.pop(0)
                males.append(male)
                continue
        # special
        male -= 2
        if male > 0:
            males.append(male)


print(f"Matches: {matches}")
if males:
    print("Males left: " + ', '.join(list(map(str, males[::-1]))))
else:
    print("Males left: none")

if females:
    print("Females left: " + ', '.join(list(map(str, females))))
else:
    print("Females left: none")