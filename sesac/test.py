def power(base, exponent):
    if exponent == 1:
        return base

    x = power(base, exponent // 2)
    if exponent % 2:
        return x * x * base
    else:
        return x * x

print(power(2, 10))