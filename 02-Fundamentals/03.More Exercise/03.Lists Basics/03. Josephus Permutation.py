soldiers = input().split()
kill_counter = int(input()) - 1
dead_soldiers = list()

i = kill_counter
while len(soldiers) > 0:
    if i >= len(soldiers):
        i -= len(soldiers)
    else:
        dead_soldiers.append(soldiers.pop(i))
        i += kill_counter

print(f"[{','.join(dead_soldiers)}]")