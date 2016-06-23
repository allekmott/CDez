class CD:
	"""
	Data structure to house CD table entry
	"""
	def __init__(self, id, artist, name, box, location):
		self.id = id
		self.artist = artist
		self.name = name
		self.box = box
		self.location = location

	def __init(self, db_row):
		self.id = db_row[0]
		self.artist = db_row[1]
		self.name = db_row[2]
		self.box = db_row[3]
		self.location = db_row[4]
