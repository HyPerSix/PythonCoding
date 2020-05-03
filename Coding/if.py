code = (input("Enter your code here : "))
password = '1234'
if code == password :
    print(f"Happy birth !!!")
    print(f"You have 10% Discount !!!")
    print("Let's shopping !!!")
    tv = int(input("TVs : "))
    dvd = int(input("DVD : "))
    audio = int(input("audio : "))
    pay = tv*3000+dvd*750+audio*1500
    discount = (10/100)*pay
    pay= pay-discount
else:
    tv = int(input("TVs : "))
    dvd = int(input("DVD : "))
    audio = int(input("audio : "))
    pay = tv*3000+dvd*750+audio*1500
print(f"You have you pay {pay} baht.")
