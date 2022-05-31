rooms = int(input())

free_chairs = 0

for room in range(rooms):
    words_l = input().split()
    chairs_in_room = len(words_l[0])
    taken_chairs = int(words_l[1])
    difference = chairs_in_room - taken_chairs
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room + 1}")
        free_chairs += difference   # free chairs --difference
    else:
        free_chairs += difference

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")

