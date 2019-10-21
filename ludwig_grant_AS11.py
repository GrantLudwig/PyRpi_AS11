# File Name: ludwig_grant_AS11.py
# File Path: /home/ludwigg/Python/PyRpi_AS12/ludwig_grant_AS11.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS12/ludwig_grant_AS11.py

# Grant Ludwig
# 10/25/2019
# AS.11
# Midterm Pot Pourri

# Program 1
weekMessage = { "Monday" : "The Way Get Started Is To Quit Talking And Begin Doing.",
				"Tuesday" : "The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.",
				"Wednesday" : "Do Not Let Yesterday Take Up Too Much Of Today.",
				"Thursday" : "You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.",
				"Friday" : "It Is Not Whether You Get Knocked Down, It Is Whether You Get Up.",
				"Saturday" : "If You Are Working On Something That You Really Care About, You Do Not Have To Be Pushed. The Vision Pulls You.",
				"Sunday" : "People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do."}
				
def encourageMe(day):
	if day in weekMessage:
		return weekMessage[day]
	else:
		return "You entered not a day of the week"
		
print(encourageMe("Friday"))

# Program 2
def areaCalcRect(length, width):
	return length * width
	
print(areaCalcRect(5, 10))

# Program 3