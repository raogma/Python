def get_primes(iterable: list):
    iterable = [x for x in iterable if x > 1]
    for num in iterable:
        isPrime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                isPrime = False
                break
        if isPrime:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))