names = ["张三", "李四", "王五"]
for name in names:
    print(name)

print("------------------------------------------")
sum = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum += i
print(sum)

print("------------------------------------------")
listSum = 0
for i in list(range(101)):
    listSum += i
print(listSum)

print("------------------------------------------")
whileSum = 0
n = 0
while n <= 100:
    whileSum += n
    n += 1
print(whileSum)

print("------------------------------------------")
breakSum = 0
n = 0
while n <= 100:
    if n == 50:
        break
    breakSum += n
    n += 1
print(breakSum)
print("-----------------打印10以内奇数-------------------------")
for x in list(range(10)):
    if x % 2 == 0:
        continue
    else:
        print(x)
