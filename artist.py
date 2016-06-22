class Artist:
	"""
	Data structure to house Artist table entry
	"""
	def __init__(self, id, name):
		self.id = id
		self.name = name

	def __init__(self, prop_list):
		self.id = prop_list[0]
		self.name = prop_list[1]