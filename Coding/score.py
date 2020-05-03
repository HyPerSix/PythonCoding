scores=[]
avg=0
count=0
while(True):
    score=(input("Enter student score (or Enter to finish):"))
    if(score==""):
        break
    else:
        score=float(score)
        scores.append(score)
        #count+=1
if(len(scores)==0):
        avg=0
else:
        avg=sum(scores)/len(scores)
for x in range(len(scores)):
    scores.sort(reverse=True)
    print(f"Student #{x+1} score: {scores[x]}")
print(f"Acverge score is = {avg:.2f}")
print(f"Minimum {min(scores)}")
print(f"Maximum {max(scores)}")
