from sys import maxsize

snowballs = int(input())

max_value = -maxsize

for snowball in range(snowballs):
    snow = int(input())
    time = int(input())
    quality = int(input())

    value = (snow / time) ** quality
    if value > max_value:
        max_value = value
        perfect_snow = snow
        perfect_time = time
        perfect_quality = quality

print(f"{perfect_snow} : {perfect_time} = {int(max_value)} ({perfect_quality})")