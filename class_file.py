
class calc:
    def __init__(self):
        print("Hello to the calculator program")
        self.numa = 0
        self.numb = 0

    def ask_numbers(self):
        print("Please enter the first number: ")
        c = int(input())
        self.numa = c
        print("Please enter the second number: ")
        d = int(input())
        self.numb = d

    def addition(self):
        return self.numa + self.numb

    def subtract(self):
        return self.numa - self.numb

    def multiply(self):
        return self.numa * self.numb

    def divide(self):
        return self.numa / self.numb


calculate = calc()
calculate.ask_numbers()
print("Please select any one of the operations: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide ")
print("")
a = int(input())
if a == 1:
    x = calculate.addition()
    print("Your sum is : ", x)
elif a == 2:
    x = calculate.subtract()
    print("Your difference is: ", x)
elif a == 3:
    x = calculate.multiply()
    print("Your product is: ", x)
elif a == 4:
    x = calculate.divide()
    print("Your quotient is: ", x)
else:
    print("Wrong Selection! Please try again")

