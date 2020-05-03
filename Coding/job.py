def get_input():
    name=input("Enter ur name : ")
    age=int(input("Enter ur age : "))
    job=input("Enter ur jobs : ")
    return name,age,job


name,age,job=get_input()

point = 0

if name[0] == 'O':
    point += 1000
    
if age <= 24:
    point = point-300
    
if job == "Student" or job == "Programmer" :
    point -= 300
   
print(point)
if point > 500 :
    print("You've got money !!!")
else:
    print("You're not passed ,sorry.")

