def ip():
    name_local=input("Enter your name : ")
    w= int(input("Enter the width : "))
    h=int(input("Enter the height : "))
    return name_local,w,h
def find_area(w,h):
    a=1/2*w*h
    return a
name,weight,height=ip()
area=find_area(weight,height)
print(f"Hello {name}, your triangle area is {area}")
