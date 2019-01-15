age = 10
if age > 18:
    print("成年了!")
else:
    print("未成年")

print("-------------------------------------------")
age = 18
print(age)
if age >= 15:
    print("成年了!")
elif age >= 18:
    print("法律上成年了!")
else:
    print("未成年")

print("-------------------------------------------")

while 1:
    a = input("请输入年龄:")
    s = int(a)
    if s == -1:
        print("您退出了输入")
        break
    if s < 18:
        print("未成年")
    elif 18 <= s <= 35:
        print("年轻力壮!")
    elif 35 < s <= 60:
        print("有点老")
    else:
        print("老年人")
print("-------------------------------------------")
# 输入身高体重,请根据BMI公式（体重除以身高的平方）计算BMI指数，并根据BMI指数打印：
#   低于18.5：过轻
#   18.5-25：正常
#   25-28：过重
#   28-32：肥胖
#   高于32：严重肥胖
height = int(input("请输入身高:"))
width = int(input("请输入体重:"))
BMI = pow(width / height, 2)
if BMI >= 18.5:
    print("有点青")
elif 18.5 < BMI <= 25:
    print("过重")
elif 25 < BMI <= 28:
    print("过重")
elif 28 < BMI <= 32:
    print("肥胖")
else:
    print("严重肥胖")
