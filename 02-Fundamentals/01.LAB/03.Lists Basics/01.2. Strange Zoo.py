tail = input()
body = input()
head = input()

strange_animal = [tail, body, head]
normal_animal = strange_animal[::-1]

print(normal_animal)