import webbrowser
import time

print("Program is start at" + time.ctime())
#creating a for loop to run 3 times
for index in range(3): 
	#print("Program is running for #" + (index + 1))
	#sleep for 10 seconds
	time.sleep(10)
	#open youtube app at the end of timer
	webbrowser.open('https://www.youtube.com/watch?v=tAGnKpE4NCI')