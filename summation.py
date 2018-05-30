import argparse

parser = argparse.ArgumentParser(description="This is our help")
parser.add_argument("-a", type=int, help="Please provide the first number", required=True)
parser.add_argument("-b", type=int, help="Please provide the next number", required=True)

#   cmdvar becomes a dictionary/hash
cmdvar = parser.parse_args()

#   using the flag to access the corresponding value
a = cmdvar.a
b = cmdvar.b
sum = a + b
diff = a - b
mult = a * b
div = a / b
print("Your sum is ", sum)
print("Your difference is ", diff)
print("Your product is ", mult)
print("Your quotient is ", div)