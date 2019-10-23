# File Name: ludwig_grant_AS11.py
# File Path: /home/ludwigg/Python/PyRpi_AS12/ludwig_grant_AS11.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS12/ludwig_grant_AS11.py

# Grant Ludwig
# 10/25/2019
# AS.11
# Midterm Pot Pourri

from graphics import *
import random

# Program 1
weekMessage = { "Monday" : "The Way Get Started Is To Quit Talking And Begin Doing.",
				"Tuesday" : "The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.",
				"Wednesday" : "Do Not Let Yesterday Take Up Too Much Of Today.",
				"Thursday" : "You Learn More From Failure Than From Success. Do Not Let It Stop You. Failure Builds Character.",
				"Friday" : "It Is Not Whether You Get Knocked Down, It Is Whether You Get Up.",
				"Saturday" : "If You Are Working On Something That You Really Care About, You Do Not Have To Be Pushed. The Vision Pulls You.",
				"Sunday" : "People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do."}
				
def encourageMe(day):
	if day in weekMessage:
		return weekMessage[day]
	else:
		return "You entered not a day of the week"

print()
print("Program 1")
print("---------")	
print("Monday:", encourageMe("Monday"))
print("Tuesday:", encourageMe("Tuesday"))
print("Wednesday:", encourageMe("Wednesday"))
print("Thursday:", encourageMe("Thursday"))
print("Friday:", encourageMe("Friday"))
print("Saturday:", encourageMe("Saturday"))
print("Sunday:", encourageMe("Sunday"))
print()
input("Press enter to continue")
print()

# Program 2
def areaCalcRect(length, width):
	return length * width
	
print("Program 2")
print("---------")	
print("Length: 5, Width: 10 Area:", areaCalcRect(5, 10))
print("Length: 100, Width: 30 Area:", areaCalcRect(100, 30))
print("Length: 17, Width: 81 Area:", areaCalcRect(17, 81))
print()
input("Press enter to continue")
print()

# Program 3
numberList = [5, 4, 3, 2, 1]

def printDecendingNumbers():
	for _ in range(len(numberList)):
		printString = ""
		for num in numberList:
			printString += str(num) + " "
		print(printString)
		del numberList[0]

print("Program 3")
print("---------")		
printDecendingNumbers()
print()
input("Press enter to continue")
print()

# Program 4
colors = ["Red",
          "Green",
          "Blue",
          "Purple",
          "Pink",
          "Yellow",
          "Orange",
          "Brown",
          "Gray",
		  "Black",
		  "White"]

win = GraphWin("Loops", 500, 500, autoflush=False)

def main():
	rectangles = []
	for i in range(6):
		for j in range(6):
			rect = Rectangle(Point(100 + i * 50, 100 + j * 50), Point(150 + i * 50, 150 + j * 50))
			rect.setFill(random.choice(colors))
			rectangles.append(rect)
	for rect in rectangles:
		rect.draw(win)
		
	win.getMouse()
	win.close()

print("Program 4")
print("---------")
main()
print()
input("Press enter to continue")
print()

# Program 5
def stringReverse(strReverse):
    returnString = ""
    for i in range(-1, -len(strReverse) - 1, -1):
        returnString += strReverse[i]
    return returnString
    
print("Program 5")
print("---------")
print("Hello there.:", stringReverse("Hello there."))
print("General Kenobi!:", stringReverse("General Kenobi!"))