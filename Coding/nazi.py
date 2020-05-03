def decode(text):
    lst = []
    txt = ""
    for i in range(len(text)):
        for j in range(len(t1)):
            if(text[i]==t1[j]):
                if(j==(len(t1)-1)):
                    lst.append(t1[0])
                    break
                else:
                    lst.append(t1[j+1])
                    break
            elif(text[i]==t2[j]):
                    if(j==(len(t2)-1)):
                        lst.append(t2[0])
                        break
                    else:
                        lst.append(t2[j+1])
                        break
            elif(text[i] in num):
                lst.append(text[i])
                break
            elif(text[i] == " "):
                lst.append(text[i])
                break
            else:
                pass
    return txt.join(lst)

def encode (text):
    lst1 = []
    txt1 = ""
    for i in range(len(text)):
        for j in range(len(t1)):
            if(text[i]==t1[j]):
                if(j==(len(t1)+1)):
                    lst1.append(t1[0])
                    break
                else:
                    lst1.append(t1[j-1])
                    break
            elif(text[i]==t2[j]):
                    if(j==(len(t2)+1)):
                        lst1.append(t2[0])
                        break
                    else:
                        lst1.append(t2[j-1])
                        break
            elif(text[i] in num):
                lst1.append(text[i])
                break
            elif(text[i] == " "):
                lst1.append(text[i])
                break
            else:
                pass
    return txt1.join(lst1)


t1 = "abcdefghijklmnopqrstuvywxyz"
t2 = t1.upper()
num = "0123456789"
number=int(input("Enter 1 or 2 (#1 = decode or 2 = encode) : "))
if number == 1 :
     tet=input("Enter ur text : ")
     print(decode(tet))
elif number == 2 :
     tet=input("Enter ur text2 : ")
     print(encode(tet))
else:
    print("Enter 1 or 2 only !!!")


