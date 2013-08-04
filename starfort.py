"""
Program: starfort.py
Author: Rishi Agarwal
Last Date Modified: 1/8/2013

The purpose of this program is to generate coordintes for creating a simple star fort island.
Example island is this: http://commons.wikimedia.org/wiki/File:Neuf_Brisach.jpg"""

from graphics import *
from math import *
def main():
  origin = [0,0,0]
	f_radius = 8
	f_octagon = [[f_radius*sin(pi/8),f_radius*cos(pi/8),0],[f_radius*cos(pi/8),f_radius*sin(pi/8),0],[f_radius*cos(pi/8),-f_radius*sin(pi/8),0],[f_radius*sin(pi/8),-f_radius*cos(pi/8),0],[-f_radius*sin(pi/8),-f_radius*cos(pi/8),0],[-f_radius*cos(pi/8),-f_radius*sin(pi/8),0],[-f_radius*cos(pi/8),-f_radius*sin(pi/8),0],[-f_radius*sin(pi/8),f_radius*cos(pi/8),0]]
	s_radius = f_radius*1.2
	s_octagon = [[s_radius*sin(pi/8),s_radius*cos(pi/8),0],[s_radius*cos(pi/8),s_radius*sin(pi/8),0],[s_radius*cos(pi/8),-s_radius*sin(pi/8),0],[s_radius*sin(pi/8),-s_radius*cos(pi/8),0],[-s_radius*sin(pi/8),-s_radius*cos(pi/8),0],[-s_radius*cos(pi/8),-s_radius*sin(pi/8),0],[-s_radius*cos(pi/8),-s_radius*sin(pi/8),0],[-s_radius*sin(pi/8),s_radius*cos(pi/8),0]]
	t_radius = s_radius*1.2
	t_octagon = [[t_radius*sin(pi/8),t_radius*cos(pi/8),0],[t_radius*cos(pi/8),t_radius*sin(pi/8),0],[t_radius*cos(pi/8),-t_radius*sin(pi/8),0],[t_radius*sin(pi/8),-t_radius*cos(pi/8),0],[-t_radius*sin(pi/8),-t_radius*cos(pi/8),0],[-t_radius*cos(pi/8),-t_radius*sin(pi/8),0],[-t_radius*cos(pi/8),-t_radius*sin(pi/8),0],[-t_radius*sin(pi/8),t_radius*cos(pi/8),0]]
	t_m_octagon=[[0,s_radius*1.3,0],[s_radius*sin(pi/4),s_radius*sin(pi/4),0],[s_radius*1.3,0,0],[s_radius*sin(pi/4),-s_radius*sin(pi/4),0],[0,-s_radius*1.3,0],[-s_radius*1.3*sin(pi/4),-s_radius*1.3*cos(pi/4),0],[-s_radius*1.3,0,0],[-s_radius*1.3*sin(pi/4),s_radius*1.3*sin(pi/4),0]]
	
	win=GraphWin();
	pt = Point(10,10)
	pt.draw(win)
	win.getMouse()
#def main():
#	win=GraphWin("My Circle", 100, 100)
#	c= Circle (Point(50,50), 10)
#	c.draw(win)
#	win.getMouse()
#	win.close()

main()
