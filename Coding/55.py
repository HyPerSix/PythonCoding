avg = 0
count = 0
summ = 0
while(True):
    score = (input("Enter student score (or Enter to finish) : "))
    if(score == ""):
        break
    else:
        score = float(score)
        summ = summ+score
        count = count+1
if(count==0):
    avg = 0
else:
    avg = summ/count
print(f"There are {count} people ,has avg = {avg:.2f}")
