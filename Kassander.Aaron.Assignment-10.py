#Aaron Kassander
#Program Written 3/9/2020 - 3/12/2020
#This program uses assignment 8 as the base but alters the graph to a
#pie chart to show percentages of value distribution between all of 
#the stock's closing costs.

#Importing the json and matplotlib libraries
import json
import matplotlib.pyplot as plt

#Assigning the json file to a name
filename = "AllStocks.json"

#Opening the json file
with open(filename) as l:
	stockname = json.load(l)

#Creating a 'for' loop to run through the list
for stock in stockname:
	#Creating date entry condition to be August 4, 2017
	if stock['Date'] in ["4-Aug-17"]:
		#Creating name entry condition to be AIG
		if stock['Symbol'] in ['AIG']:
			#Assigning stock close data to variable
			AIG_Data = (float (stock['Close']))
		#Creating name entry condition to be F
		elif stock['Symbol'] in ['F']:
			#Assigning stock close data to variable
			F_Data =(float (stock['Close']))
		#Creating name entry condition to be FB
		elif stock['Symbol'] in ['FB']:
			#Assigning stock close data to variable
			FB_Data = (float (stock['Close']))
		#Creating name entry condition to be GOOG
		elif stock['Symbol'] in ['GOOG']:
			#Assigning stock close data to variable
			GOOG_Data = (float (stock['Close']))
		#Creating name entry condition to be IBM
		elif stock['Symbol'] in ['IBM']:
			#Assigning stock close data to variable
			IBM_Data = (float (stock['Close']))
		#Creating name entry condition to be M
		elif stock['Symbol'] in ['M']:
			#Assigning stock close data to variable
			M_Data = (float (stock['Close']))
		#Creating name entry condition to be MSFT
		elif stock['Symbol'] in ['MSFT']:
			#Assigning stock close data to variable
			MSFT_Data = (float (stock['Close']))
		#Creating name entry condition to be RDS
		elif stock['Symbol'] in ['RDS-A']:
			#Assigning stock close data to variable
			RDS_Data =(float (stock['Close']))

#The slices of the pie will be ordered and plotted counter-clockwise
#Setting labels for each section of the pie chart
labels = 'AIG', 'F', 'FB', 'GOOG', 'IBM', 'M', 'MSFT', 'RDS-A'
#Entering data from variables to accompanying slice of pie
#The data is entered in the same order as the labels
sizes = [AIG_Data, F_Data, FB_Data, GOOG_Data, IBM_Data, M_Data, MSFT_Data, RDS_Data]
#Adjusting placement of Google slice to stand out more in pie chart
explode = [0, 0, 0, 0.05, 0, 0, 0, 0]
#Creating the pie chart
plt.pie(sizes, autopct='%1.1f%%', explode = explode)
#Adding title to the pie chart
plt.title("Stock Value Distribution for August 4, 2017")
#Adding axis to make sure pie chart is complete circle
plt.legend(labels, loc=3)
plt.axis('equal')
#Showing the pie chart
plt.show()
