import webbrowser

class Movie():

	"""This class is a way of creating Movie instances"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, title, story, poster_url, youtube_url):
		self.title = title
		self.story = story
		self.poster_image_url = poster_url
		self.trailer_youtube_url = youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
