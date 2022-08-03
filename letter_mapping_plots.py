import numpy as np
import math
import matplotlib.pyplot as plt

#Defining robot drawing area (mm) (avg letter width = 100mm)
ybase = 200
ymax = 300
xbase = -100
xmax = 100

diameter = (abs(xbase)+abs(xmax))/2
radius = diameter/2
width = 50

#Offest is used when writing the second letter (translate letter to thr right 100 mm)
offset = 100

#This fuction finds equally spaced points on a straight line from a start point to an end point
def DrawStraightLine(start, end, num_points):
	return np.linspace(start, end, num_points)

# Draw the leffter R 
def DrawR(num_points):

	topx = np.cos(np.linspace(math.pi / 2, math.pi * 3 / 2 , num_points))
	topy = np.sin(np.linspace(math.pi / 2, math.pi * 3 / 2, num_points))

	topx *= xbase/2
	topy *= radius/2
	topx -= xmax
	topy += ybase + (ymax-ybase)/2 + radius/2

	line_up = DrawStraightLine([xbase, ybase], [xbase, ymax], num_points)
	line_down_across = DrawStraightLine([xbase, ybase+(ymax-ybase)/2], [xbase+width, ybase], num_points)

	plt.plot(topx, topy, marker = 'o')
	plt.plot(line_up[:,0], line_up[:,1], marker = 'o')
	plt.plot(line_down_across[:,0], line_down_across[:,1], marker = 'o')

	plt.xlim(xbase-50, xmax+50)
	plt.ylim(ybase-50, ymax+50)
	#plt.show()

# Draw the letter G 
def DrawG(num_points):
	x = np.cos(np.linspace(math.pi / 2, math.pi * 2 , num_points))
	y = np.sin(np.linspace(math.pi / 2, math.pi * 2, num_points))

	x *= radius/2
	y *= radius
	x -= xbase + radius
	y += ybase + radius

	line_across = DrawStraightLine([(xbase+xmax)/2+width, ybase+(ymax-ybase)/2],[xbase/4+offset, ybase+(ymax-ybase)/2], num_points)


	plt.plot(x,y, marker = 'o')
	plt.plot(line_across[:,0], line_across[:,1], marker = 'o')

	plt.show()

# Draw the letter B
def DrawB(num_points):
	line_up = DrawStraightLine([xbase, ybase], [xbase, ymax], num_points)

	topx = np.cos(np.linspace(math.pi / 2, math.pi * 3 / 2 , num_points))
	topy = np.sin(np.linspace(math.pi / 2, math.pi * 3 / 2, num_points))

	topx *= -radius
	topy *= radius/2
	topx += xbase
	topy += ybase + (ymax-ybase)/2 + radius/2

	bot_halfcircle_x = np.cos(np.linspace(math.pi / 2, math.pi * 3 / 2 , num_points))
	bot_halfcircle_y = np.sin(np.linspace(math.pi / 2, math.pi * 3 / 2, num_points))

	bot_halfcircle_x *= -radius
	bot_halfcircle_y *= radius/2
	bot_halfcircle_x += xbase
	bot_halfcircle_y += ybase + radius/2

	plt.plot(topx, topy, marker="o")
	plt.plot(bot_halfcircle_x, bot_halfcircle_y, marker="o")
	plt.plot(line_up[:, 0], line_up[:, 1], marker="o")

	plt.xlim(xbase-50, xmax+50)
	plt.ylim(ybase-50, ymax+50)
	#plt.show()

# Draw the letter M
def DrawM(num_points):
	line_up = DrawStraightLine([xbase+offset, ybase], [xbase+offset, ymax], num_points)
	line_down_across =  DrawStraightLine([xbase + offset, ymax], [(xbase + offset + xmax) / 4 , (ybase + ymax) / 2], num_points)
	line_up_across =  DrawStraightLine([(xbase + offset + xmax) / 4, (ybase + ymax) / 2], [xmax/2, ymax], num_points)
	line_down = DrawStraightLine([xmax/2, ymax], [xmax/2, ybase], num_points)

	plt.plot(line_up[:, 0], line_up[:, 1], marker="o")
	plt.plot(line_down_across[:, 0], line_down_across[:, 1], marker="o")
	plt.plot(line_up_across[:, 0], line_up_across[:, 1], marker="o")
	plt.plot(line_down[:, 0], line_down[:, 1], marker="o")
	plt.show()

# Draw the letter T
def DrawT(num_points):
	line_up = DrawStraightLine([xbase+xmax/2, ybase], [xbase+xmax/2, ymax], num_points)
	line_across = DrawStraightLine([xbase, ymax], [(xbase+xmax)/2, ymax], num_points)

	plt.plot(line_up[:, 0], line_up[:, 1], marker="o")
	plt.plot(line_across[:, 0], line_across[:, 1], marker="o")
	
	plt.xlim(xbase-50, xmax+50)
	plt.ylim(ybase-50, ymax+50)
	#plt.show()

# Draw the letter K
def DrawK(num_points):
	line_up = DrawStraightLine([xbase+offset, ybase], [xbase+offset, ymax], num_points)
	line_up_across =  DrawStraightLine([xbase+offset, (ybase + ymax) / 2], [(xbase+xmax)/2+offset, ymax], num_points)
	line_down_across =  DrawStraightLine([xbase+offset, (ybase + ymax) / 2], [(xbase+xmax)/2+offset, ybase], num_points)

	plt.plot(line_up[:, 0], line_up[:, 1], marker="o")
	plt.plot(line_down_across[:, 0], line_down_across[:, 1], marker="o")
	plt.plot(line_up_across[:, 0], line_up_across[:, 1], marker="o")
	plt.show()

DrawB(100)
DrawM(100)

