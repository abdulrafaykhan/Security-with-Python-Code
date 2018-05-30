import argparse

parser = argparse.ArgumentParser(description="This is our description")
parser.add_argument('-i', type=str, help="This is the help you get to describe the parameter", required=False)
parser.add_argument('-o', type=str, help="This is optional", required=False)

#   cmdargs ends up being a dictionary
cmdargs = parser.parse_args()

#   access the parameters based on flags
ivar = cmdargs.o
print(ivar)