class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("Last name - "+ self.last_name)
		print("Eye color - "+ self.eye_color)

class Child(Parent):
	def __init__(self, last_name, eye_color, numberOfToys):
		print("Child constructor called")
		Parent.__init__(self, last_name, eye_color)
		self.numberOfToys = numberOfToys

	def show_info(self):
		print("Last name - "+ self.last_name)
		print("Eye color - "+ self.eye_color)
		print("Number of Toys - "+str(self.numberOfToys))

#billy_cyrus = Parent("cyrus", "blue")
#print(billy_cyrus.last_name)

miley_cyrus = Child("cyrus", "blue", 5)
miley_cyrus.show_info()