command = input()
prime_sum = 0
non_prime_sum = 0

while command != "stop":
    number = int(command)
    isPrime = True
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    else:
        for divider in range(2, number):
            if number % divider == 0:
                isPrime = False
                break
    if isPrime:
        prime_sum += number
    else:
        non_prime_sum += number

    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")