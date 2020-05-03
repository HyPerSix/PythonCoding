def register():
    uname= input("Enter username : ")
    while True:
        if (uname =="" or len(uname)<6):
            print("Please try again !")
            uname=input("Enter username : ")
        else:
            break
    upass= input("Enter password : ")
    while True:
        if (upass =="" or len(upass)<6):
            print("Please try again !")
            upass=input("Enter password : ")
        else:
            break
    name=input("Enter your name : ")
    user.append([uname,upass,name])

def sign_in():
    uname=input("Enter username to login : ")
    ii=-1
    while True:
        for i in range(len(user)):
            if(uname==user[i][0]):
                ii=i
                break
        if(ii==-1):
            print("User not fonud")
            uname=input("Enter username to login : ")
        else:
            break
    upass=input("Enter password to login : ")
    while(True):
        if(upass==user[ii][1]):
            print(f"Ok you're in")
            return "Success"
        else:
            print("Pasword not found \nPlease try again !")
            upass=input("Enter password to login : ")

    
user=[]
