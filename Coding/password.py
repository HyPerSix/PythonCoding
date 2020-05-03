def check_password(x):
    if(x==password):
        return x
    else:
        return check_password(x+1)

import random
password = random.randrange(0,1000)
