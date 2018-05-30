def subr():
    x = 1
    a = 2
    y = a + x
    print(y)
    print(x)
    return y

x = 12


for i in range(12, 23):
    x = i + x

subr()
print(x)