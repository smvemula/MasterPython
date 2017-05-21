import os

def rename_files():
	file_list = sorted(os.listdir("/Users/mm/Downloads/prank"))
	#print file_list
	saved_path = os.getcwd()
	print ("Current Working Directory:" + saved_path)
	os.chdir("/Users/mm/Downloads/prank")
	for file_name in file_list:
		print ("Old name - "+ file_name)
		print("New name - "+ file_name.translate(None, "0123456789"))
		os.rename (file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)
rename_files()