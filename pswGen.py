from random import choice
import string


size = int(input('Set a number of the size in the your password '))
params = string.ascii_letters + string.digits + string.punctuation
psw = ''
for i in range(size):
  psw += choice(params)

print(psw)