def add():
    iname=input("Enter item name : ")
    while True:
        if iname.upper()=="":
            print("Please try again !!!")
            iname=input("Enter item name : ")
        else:
            break
    itemm=int(input("How many item ? : "))
    cost=float(input(f"How much {iname} ? : "))
    
    ii=-1
    while True:
        for i in range(len(item)):
            if iname.upper()==item[i][0]:
                item[i][1]+=itemm
                ii=i
                break
        if ii==-1:
            item.append([iname.upper(),itemm,cost])
            break
        else:
            break
        


def customer():
    print("Welcome to our shop !!!")
    want=input("Whice item do you want ? : ")
    ii=-1
    while True:
        for n in range(len(item)):
            if want.upper()==item[n][0]:
                ii=n
                break
            else:
                break
                
        if ii==-1:
            print("Item not found")
            print("Please try again !")
            want=input("Whice item do you want ? : ")
        else:
            break
    while True:
        if want.upper()==item[ii][0]:
            print(f"The {item[ii][0]} avaliable for {item[ii][1]}")
            break
        else:
            break
    need=input("Do you need it ? (y or n) : ")
    while True:
        if need.upper()=="Y" or need.upper()=="YES":
            break
        elif need.upper()=="N" or need.upper()=="NO":
            print("We'll be welcome again")
            break
        else:
            break
    much=int(input("How much you need it ? : "))
    while True:
        if much>item[ii][1]:
            print("Item is not enough please try again !")
            much=int(input("How much you need it ? : "))
        else:
            print(f"You have to pay for {much*item[ii][2]:.2f} baht")
            break
    pay=input("Are u paying it ? (y or n) : ")
    while True:
        if pay.upper()=="Y" or pay.upper()=="YES":
            item[ii][1]-=much
            print("Thanks for purchase !!!")
            break
        elif pay.upper()=="N" or pay.upper()=="NO":
            print("We'll be welcome again")
            break
        else:
            break



item=[]






