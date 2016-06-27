class Artist:
	"""
	Data structure to house Artist table entry
	Instance vars:
	id		ID of Artist in database
	name	Name of Artist7
	"""
	def __init__(self, id, name):
		self.id = id
		self.name = name

	def __init__(self, db_row):
		self.id = db_row[0]
		self.name = db_row[1]

	def __str__(self):
		"""
		Override string representation of object
		"""
		return "%i\t%n" % (self.id, self.name)