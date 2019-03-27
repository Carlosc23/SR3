# Carlos Calderon, 15219
# SR2 Lines
# Program that create a lines with bresenham algorithm
import sys

from SR1 import SoftwareRender


xo, yo, xf, yf = -1, -1, 1, 1
x = SoftwareRender('out.bmp')
x.glCreateWindow(1000, 1000)
x.glViewPort(0, 0, 1000, 1000)
x.glClear()
x.glColor(1, 0, 0)
x.glVertex(0, 0)
#x.glLine(xo, yo, xf, yf)
x.load('./models/mushroom.obj', (4, 3), (100, 100))
#x.load('./models/face.obj', (25, 5), (15, 15))
x.glFinish()
