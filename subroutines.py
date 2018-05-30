def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x/y

print('Please select any one of the operations:')
print('1. Subtraction')
print('2. Addition')
print('3. Multiply')
print('4. Divide')
p = input()
p = int(p)
a = input('Please enter the first integer')
a = int(a)
b = input('Please enter the second integer')
b = int(b)
print("Your result is: ")
if p == 1:
    print(add(a, b))
elif p == 2:
    print(sub(a, b))
elif p == 3:
    print(mult(a, b))
else:
    print(div(a, b))
