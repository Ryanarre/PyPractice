import sys

def is_prime(number):
    div_count = 0
    for x in range(number):
        if number % (x+1) == 0:
            div_count += 1
        if div_count > 2:
            return False
    return True

print(is_prime(123))
print(is_prime(97))