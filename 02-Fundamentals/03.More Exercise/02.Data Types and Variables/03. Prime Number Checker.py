def check_for_prime(number):
    for divider in range(2, number):
        return False if number % divider == 0 else True


num = int(input())
print(check_for_prime(num))
