LAB = "turtlelab2x.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab2x import turtle,home,shop,check
from turtle import forward as fw
from turtle import backward as bw
from turtle import left as lf
from turtle import right as rt
# Put your turtle movement commands here
fw(shop.x)
lf(90)
fw(shop.y)
rt(90)
fw(home.x-shop.x)
lf(90)
fw(home.y-shop.y)
# ______________________________________
# ______________________________________
# ______________________________________

check()
