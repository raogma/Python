# prime - просто число > 1, има точно 2 делителя – 1 и самото себе си
# Пример: 5
# non - prime - непросто число
# Пример: 6

command = input()

prime_sum = 0
non_prime_sum = 0

while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
    elif number % 2 == 0 and number != 2 or number % 3 == 0 and number != 3:
        non_prime_sum += number
    else:
        prime_sum += number
    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")