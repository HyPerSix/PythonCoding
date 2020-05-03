LAB = "turtlelab1.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.4",LAB)

from turtlelab1 import turtle,check
from turtle import forward as fw
from turtle import backward as bw
from turtle import left as lf
from turtle import right as rt
# Put your turtle movement commands here
fw(30)
lf(60)
lf(5)
lf(3)
fw(120)
fw(60)
fw(5)
fw(10)
fw(5)
lf(30)
fw(5)
fw(10)

# ______________________________________
# ______________________________________
# ______________________________________

check()
