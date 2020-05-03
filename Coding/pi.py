import math
def r():
    x=int(input("Enter radious : "))
    return x
def calculate(d):
    pi=math.pi*d*d
    return pi

radious =r()
p=calculate(radious)
print(f"your pi = {p:.2f}")
