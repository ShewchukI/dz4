def factorial(f):
    if f == 0 or f == 1:
        return 1
    else:
        return f * factorial(f - 1)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
