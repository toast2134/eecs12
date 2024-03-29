# Name: Jonathan Le
# Date: Nov 8, 2021

from graphics import *
from time import *
import random

# given top and lower left corner, draw the tires and car body
def draw_car(win,p1,p2):
	# list that contains each car element
	carlist1=[]
	
	# drawing the left tire
	tire_left = Circle(Point(p1.x+abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
	tire_left.setFill("black")
	tire_left.draw(win)
	carlist1.append(tire_left)
	
	# drawing the right tire
	tire_right = Circle(Point(p2.x-abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
	tire_right.setFill("black")
	tire_right.draw(win)
	carlist1.append(tire_right)
	
	# car body
	body = Rectangle(p1,p2)
	body.setFill("blue")
	body.draw(win)
	carlist1.append(body)
	
	# function returns "car" as list of individual parts
	return carlist1

# draws the roof of each vehicle but depends on the vehicle type
def draw_vehicle_roof(win, p1, p2, p3, cartype):
	carlist=[]

	# car type 1 refers to a car with a trapezoidal roof
	if cartype==1:
		car_roof = Polygon(Point(p1.x+abs(p2.x-p1.x)/4,p2.y),Point(p2.x-abs(p2.x-p1.x)/4,p2.y),Point(p2.x-3*abs(p2.x-p1.x)/8,p3.y),Point(p1.x+3*abs(p2.x-p1.x)/8,p3.y))
		car_roof.setFill("red")
		car_roof.draw(win)
		carlist.append(car_roof)

	# car type 2 refers to a truck with a rectangular roof
	if cartype==2:
		truck_roof = Rectangle(Point(p1.x+abs(p2.x-p1.x)/2,p2.y),Point(p2.x,p3.y))
		truck_roof.setFill("orange")
		truck_roof.draw(win)
		carlist.append(truck_roof)

	# returns "car" as list of individual parts (just to have it be a list)
	return carlist

# function to draw truck 
def draw_truck(win,p1,p2):
	buslist=[]
	
	# left tire for truck
	tire_left = Circle(Point(p1.x+abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
	tire_left.setFill("black")
	tire_left.draw(win)
	buslist.append(tire_left)
	
	# right tire for truck
	tire_right = Circle(Point(p2.x-abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
	tire_right.setFill("black")
	tire_right.draw(win)
	buslist.append(tire_right)
	
	# body of truck
	body = Rectangle(p1,p2)
	body.setFill("yellow")
	body.draw(win)
	buslist.append(body)
	
	# called "bus" but functions the same as "carlist"
	return buslist

# function to draw buildings in background
def draw_buildings(win, p1_x,p1_y,p2_x,p2_y,color):
    shape=Rectangle(Point(p1_x,p1_y),Point(p2_x,p2_y))
    shape.setFill(color)
    shape.draw(win)

# function to create buttons (provided by teacher)
def createButtons(win, anchor, width, height):
    button_list = [ ]
    label = ["Day", "Night", "Speed-Up", "Exit"]

    for i in range(4):
        anchor1 = anchor.clone()
        anchor2 = anchor.clone()
        anchor2.move(width, height)
        newbutton = Rectangle(anchor1, anchor2)
        newbutton.setFill("gray")
        newbutton.draw(win)
        anchor1.move(width/2, height/2)
        newlabel = Text(anchor1, label[i])
        newlabel.setStyle("bold")
        newlabel.setTextColor("white")
        newlabel.draw(win)
        if i==2:
            newlabel_special=newlabel
        button_list.append(newbutton)
        anchor.move(width+1, 0)

    return button_list, newlabel_special

# function to detect when a button is clicked
def isHitBtn(pclick, btn):
	x=pclick.x
	y=pclick.y
	if x>btn.p1.getX()and x<btn.p2.getX()and y>btn.p1.getY()and y<btn.p2.getY():
		return True
	else:
		return False

# main function
def main():
	# setting up graphics window
	win = GraphWin("City View!", 800, 600)
	win.setCoords(0, 0, 40, 30)

	# creating background and ground
	bg = Rectangle(Point(0,15), Point(40, 30))
	bg.setFill("light blue")
	bg.draw(win)

	ground = Rectangle(Point(0,6) , Point(40, 14))
	ground.setFill("light grey")
	ground.draw(win)
	temp=4
    
	# function to create street
	while temp<40:
		gnd_lines = Line(Point(temp,10),Point((temp+4),10))
		gnd_lines.setFill("white")
		gnd_lines.setOutline("white")
		gnd_lines.draw(win)
		temp+=10

	# function to create sun
	sun = Circle(Point(37,27), 2)
	sun.setFill("yellow")
	sun.setOutline("yellow")
	sun.draw(win)

	# function to create moon
	moon = Circle(Point(37,27), 2)
	moon.setFill("white")
	moon.setOutline("white")
    
	# code to set moon phase (two circles overlapping)
	mphase = Circle(Point(37.75,28),1.5)
	mphase.setFill("navy")
	mphase.setOutline("navy")

	# read input file for building sizes
	with open('input.txt','r') as file:
     # reading each line in the file
		for line in file:
			l=line.split()
			draw_buildings(win,l[0],l[1],l[2],l[3],l[4])
		file.close()

	# what kind of day displayed at the top
	txtMsg1 = Text(Point(20, 29), "Sunny Day")
	txtMsg1.setStyle("bold")
	txtMsg1.setTextColor("orange")
	txtMsg1.draw(win)

    # === set text for asking user to click a point ===
	pntMsg = Point(20, 5)
	txtMsg = Text(pntMsg, "Please click the left bottom point of the car body.")
	txtMsg.setStyle("bold")
	txtMsg.setTextColor("red")
	txtMsg.draw(win)
    # === get the point from mouse ===
	p1 = win.getMouse()
    
	txtMsg.setText("Now click the upper right point of the car body.")
	p2 = win.getMouse()
	
	# drawing the car using the two points given
	e1=draw_car(win, p1, p2)

    # === change the text to ask user to click another point ===
	txtMsg.setText("Now click the roof top point of the car.")
	p3 = win.getMouse()

	# drawing the roof of the car
	e2=draw_vehicle_roof(win, p1, p2, p3, 1)
	# e1 and e2 corresponding to the lists generated from the functions
	# car does not move

	# repeat for truck but truck moves
	txtMsg.setText("Now click the lower left point of the truck body.")
	p1 = win.getMouse()
	txtMsg.setText("Now click the upper right point of the truck body.")
	p2 = win.getMouse()
	e1=draw_truck(win,p1,p2)
	txtMsg.setText("Now click the roof top point of the truck.")
	p3 = win.getMouse()
	e1=e1+draw_vehicle_roof(win,p1,p2,p3,2)

	# remove prompts
	txtMsg.undraw()
	
	# creates buttons
	buttons,special_label = createButtons(win, Point(2,2), 4, 2)

	gameState = 0 # 0 for sunny day, 1 for moon night, 2 for sunny windy day, 3 for moon windy night
	speed = 0.05 # This speed is a variable that you can tune to see differences in speed

	# while the "display" is running
	while True:
		sleep(0.0001)

		# moves each "part" in the truck together 
		for part in e1:
			part.move(speed,0)
			if part.getP1().getX()>45:
				part.move(-47,0)

		# checks for button clicks
		pClick = win.checkMouse()
		if pClick is not None:
			# Exit button, breaks out of the loop
			if isHitBtn(pClick, buttons[3]):
				break
				
			# switch to Day state -> functions depends on previous state
			elif isHitBtn(pClick, buttons[0]):

				# if game state is windy day or sunny day, do nothing
				if gameState==0 or gameState==2:
					continue

				# if game state is night time -> undraw moon and then draw moon to set to day state
				elif gameState==1:
					moon.undraw()
					mphase.undraw()
					sun.draw(win)
					bg.setFill("light blue")
					gameState=0

				# same if game state is windy night, speed changes, and it switches to windy day instead of just day.
				elif gameState==3:
					moon.undraw()
					mphase.undraw()
					sun.draw(win)
					bg.setFill("light blue")
					speed=0.3
					gameState=2
				
			# switch to Day state -> functions depends on previous state
			elif isHitBtn(pClick, buttons[1]):

				# if game state is night or windy night -> do nothing
				if gameState==1 or gameState==3:
					continue

				# if game state is day time -> undraw sun then draw moon
				elif gameState==0:
					sun.undraw()
					moon.draw(win)
					mphase.draw(win)
					bg.setFill("navy")
					gameState=1

				# if game state is windy day -> change speed and set to "night" just like before
				elif gameState==2:
					sun.undraw()
					moon.draw(win)
					mphase.draw(win)
					bg.setFill("navy")
					speed=0.15
					gameState=3

			# speed up / slow down buttons
			elif isHitBtn(pClick, buttons[2]): 
				if gameState==0:
					speed=0.3
					special_label.setText("Slow Down")
					gameState=2
				elif gameState==1:
					speed=0.15
					special_label.setText("Slow Down")
					gameState=3
				elif gameState==2:
					speed=0.05
					special_label.setText("Speed-Up")
					gameState=0
				elif gameState==3:
					speed=0.05
					special_label.setText("Speed-Up")
					gameState=1
			
			# text message at the top
			if gameState == 0: 
				txtMsg1.setText("Sunny Day")
			elif gameState == 1: 
				txtMsg1.setText("Moon Night")
			elif gameState == 2: 
				txtMsg1.setText("Sunny Day, High Speed")
			elif gameState == 3: 
				txtMsg1.setText("Moon Night, Medium Speed")

	# close window when exit
	win.close()

# a more secure way of calling main()
if __name__ == '__main__':
    main()
    

