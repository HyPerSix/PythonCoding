msg = input("Enter a string : ")
tab=""
for i in range(len(msg)):
    print(f"{tab}{msg[i]}")
    tab+=" "
