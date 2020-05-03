salad = int(input("Enter salad price : "))
soup = int(input("Enter soup price : "))
steak = int(input("Enter steak price : "))
wine = int(input("Enter wine price : "))
oj = int(input("Enter oj price : "))
num = int(input("Enter num : "))
total = salad+soup+steak+wine+oj
total = total/num
percent_discont = int(input("Enter percent discont : "))
discont = (percent_discont/100)*total
print("you have to pay abot : ",total)
