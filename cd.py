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

	def __init(self, prop_list):
		self.id = prop_list[0]
		self.artist = prop_list[1]
		self.name = prop_list[2]
		self.box = prop_list[3]
		self.location = prop_list[4]
