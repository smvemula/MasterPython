import urllib

def read_text():
	quotes = open("/Users/mm/Desktop/MasterPython/test.txt")
	content_of_file = quotes.read()
	#print (content_of_file)
	quotes.close()
	check_profanity(content_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+ text_to_check)
	response = connection.read()
	print("Profanity check is " + response)
	if "true" in response:
		print ("Profanity Alert!!!")
	elif "false" in response:
		print("Good to Go!!!")
	else:
		print("Could not scan the document!")

	connection.close()

read_text()