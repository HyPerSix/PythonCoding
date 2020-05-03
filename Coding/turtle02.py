LAB = "turtlelab2.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.1",LAB)

from turtlelab2 import turtle,home,check
from turtle import forward as fw
from turtle import backward as bw
from turtle import left as lf
from turtle import right as rt
# Put your turtle movement commands here
rt(90)
fw(-home.y)
rt(90)
fw(-home.x)
# ______________________________________
# ______________________________________
# ______________________________________

check()
