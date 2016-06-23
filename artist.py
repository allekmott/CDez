class Artist:
	"""
	Data structure to house Artist table entry
	"""
	def __init__(self, id, name):
		self.id = id
		self.name = name

	def __init__(self, db_row):
		self.id = db_row[0]
		self.name = db_row[1]