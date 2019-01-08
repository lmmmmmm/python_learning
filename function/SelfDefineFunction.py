def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

print(my_abs(-1))


# param check
def my_abs_check(x):
    if not isinstance(x,(int,float)):
        raise TypeError('error:0.0')
    if x < 0:
        return -x
    else:
        return x


# print(my_abs_check("A"))

#return more value
def quadratic(a, b, c):
    n = 5
    return n * a, b * n, c * n

print(quadratic(1,2,3))

