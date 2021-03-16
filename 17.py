def mult_of_7(n):
    if n >= 0:
        n = n
    else:
        n = -n
    if n <= 10 and n != 0 and n != 7:
        return False
    elif n == 0 or n == 7:
        return True
    return mult_of_7((n // 10) - (2 * (n % 10)))
print(mult_of_7(1234))
print(mult_of_7(35))
print(mult_of_7(36))
print(mult_of_7(7))
print(mult_of_7(10))
print(mult_of_7(77))