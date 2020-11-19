import random
s = "abcdefghijkl\mnopqrstuvwxyz\123456789098\IBICVCBCRGCCC\dcibb#$#%^&%^"
passwordlen = 8
password = "".join(random.sample(s,passwordlen))
print(password)
