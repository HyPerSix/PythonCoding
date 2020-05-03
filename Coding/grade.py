point=int(input("Enter your point here ! : "))
if(point >= 80):
    grade = 4.00
elif(75<=point<80):
    grade = 3.5
elif(70<point<75):
    grade = 3.00
elif(65<=point<70):
    grade = 2.5
elif(60<point<65):
    grade = 2.00
elif(55<=point<60):
    grade = 1.5
elif(50<=point<55):
    grade = 1.00
else:
    grade = 0
    
print(f"Your grade is {grade}")
