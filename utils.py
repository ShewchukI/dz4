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
<<<<<<< HEAD
<<<<<<< Updated upstream
=======
=======
>>>>>>> dev5

# utils.py
def is_power_of_five(a):
    return a > 0 and (a & (a - 1)) == 0 and a % 5 == 0


<<<<<<< HEAD
def is_power_of_two(b):
    return b > 0 and (b & (b - 1)) == 0


>>>>>>> Stashed changes
=======
>>>>>>> dev5
