import random
import os


angl = "abcdefghijklmnopqrstuvwxyz"
ANGL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
int = "0123456789"
symbol = "()[]{}'/,_-!&"

all = angl + ANGL + int + symbol
length = 12
password = "".join(random.sample(all,length))
print(password)

file = open('pass.txt', 'w')
file.write(password)
file.close()
input()
