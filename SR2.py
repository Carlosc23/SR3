# Carlos Calderon, 15219
# SR2 Lines
# Program that create a lines with bresenham algorithm
import sys

from SR1 import SoftwareRender


xo, yo, xf, yf = -1, -1, 1, 1
x = SoftwareRender('out.bmp')
x.glCreateWindow(600, 600)
x.glViewPort(50, 50, 499, 499)
x.glClear()
x.glColor(1, 0, 0)
x.glVertex(0, 0)
x.glLine(xo, yo, xf, yf)
x.glFinish()
