from collections import deque


def solution(effects, explosions):
    while len(explosions) != 0 and len(effects) != 0:
        explosion = explosions.pop()
        effect = effects.popleft()
        sum = explosion + effect
        if sum % 5 == 0 and sum % 3 == 0:
            data['Crossette Fireworks'] += 1
        elif sum % 3 == 0 and sum % 5 != 0:
            data['Palm Fireworks'] += 1
        elif sum % 5 == 0 and sum % 3 != 0:
            data['Willow Fireworks'] += 1

        else:
            effect -= 1
            if effect > 0:
                effects.append(effect)
            explosions.append(explosion)
        if data['Palm Fireworks'] >= 3 and data['Willow Fireworks'] >= 3 and data['Crossette Fireworks'] >= 3:
            print("Congrats! You made the perfect firework show!")
            return
    print("Sorry. You can't make the perfect firework show.")


data = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}

effects = deque(x for x in map(int, input().split(', ')) if x > 0)
explosions = deque(x for x in map(int, input().split(', ')) if x > 0)

solution(effects, explosions)

if effects:
    print(f"Firework Effects left: {', '.join(list(map(str, effects)))}")
if explosions:
    print(f"Explosive Power left: {', '.join(list(map(str, explosions)))}")

[print(f"{key}: {value}") for key, value in data.items()]
