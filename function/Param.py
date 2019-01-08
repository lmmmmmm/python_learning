def power(x):
    return x * x

print(power(12))

def power1(x,n):
    sum = 1
    while n > 0:
        n = n - 1
        sum = sum * x
    return sum

print(power1(5,2))

# default param
def defaultParam(x,n=2):
    sum = 1
    while n > 0:
        n = n - 1
        sum = sum * x
    return sum
print(defaultParam(3,3))