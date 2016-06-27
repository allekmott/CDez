class CD:
	"""
	Data structure to house CD table entry
	Instance vars:
	id			ID of CD in database
	artist		(currently) ID of Artist in database
	name		Name of CD
	box			Box housing CD
	location	Position in housing box
	"""
	def __init__(self, id, artist, name, box, location):
		"""
		For tedious initialization: parameter by parameter
		"""
		self.id = id
		self.artist = artist
		self.name = name
		self.box = box
		self.location = location

	def __init__(self, db_row):
		"""
		For simplistic initialization: by database row
		"""
		self.id = db_row[0]
		self.artist = db_row[1]
		self.name = db_row[2]
		self.box = db_row[3]
		self.location = db_row[4]

	def __str__(self):
		"""
		Override string representation of object
		"""
		return "%i\t%i\t%s\t%s\t%s" % (self.id, self.artist, self.name, self.box, self.location)
