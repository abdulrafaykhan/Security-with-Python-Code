import os
from subprocess import call

os.chdir("D:/Practice Programming/Security with Python Code/Practice Code")
os.system("mkdir Hello")
print(os.listdir())
os.rmdir("D:/Practice Programming/Security with Python Code/Practice Code/Hello")
print(os.listdir())
