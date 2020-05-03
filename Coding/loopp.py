msg = input("What do you want me to say? ")
num = int(input("How many times you want me to say it? "))
for i in range(num):
    print(f"{msg} #{i+1}")
