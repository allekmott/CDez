import sqlite3

from artist import Artist
from cd import CD

class Database:
	@staticmethod
	def create_db(db_path):
		"""
		Create and initialize new database file with name
		designated in db_path;
		Called upon discover of database nonexistence
		"""

		# connect
		con = sqlite3.connect(db_path)

		# get cursor
		c = con.cursor()

		# create tables
		try:
			# write command to create CDs
			c.execute('''CREATE TABLE CDs
				(
					ID INTEGER PRIMARY KEY,
					Artist INT,
					Name TEXT,
					Box TEXT,
					Location TEXT
				)''')
		except sqlite3.OperationalError:
			print("Unable to create table 'CDs'")

		try:
			# write command to create Artists
			c.execute('''CREATE TABLE Artists
				(
					ID INTEGER PRIMARY KEY,
					Name TEXT NOT NULL
				)''')
		except sqlite3.OperationalError:
			print("Unable to create table 'Artists'")

		# Execute SQL commands
		con.commit()
		con.close()

	def __init__(self):
		"""
		Create database object (initialize connection, get cursor)
		"""
		self.con = sqlite3.connect("cdez.db")
		self.c = self.con.cursor()

	# facilities to provide for clean destruction of object
	def __enter__(self):
		return self
	def __exit__(self, exec_type, exec_value, traceback):
		"""
		Close database connection upon destruction of DB object
		"""
		self.con.close()

	def createArtist(self, name):
		"""
		Insert new Artist into database
		"""
		t = (name,)
		try:
			self.c.execute('''INSERT INTO Artists
				(
					ID,
					Name
				)
				VALUES (
					NULL,
					?
				)''', t)
		except sqlite3.OperationalError:
			print("Unable to insert artist '%s' into database") % name
			return

		self.con.commit()

	def createArtist(self, name):
		"""
		Insert new Artist into database
		"""
		t = (name,)
		try:
			self.c.execute('''INSERT INTO Artists
				(
					ID,
					Name
				)
				VALUES (
					NULL,
					?
				)''', t)
		except sqlite3.OperationalError:
			print("Unable to insert artist '%s' into database") % name
			return

		self.con.commit()

	def createCD(self, artist, name, box, location):
		"""
		Insert new CD into database
		"""
		t = (artist, name, box, location,)
		try:
			self.c.execute('''INSERT INTO CDs
				(
					ID,
					Artist,
					Name,
					Box,
					Location
				)
				VALUES
				(
					NULL,
					?,
					?,
					?,
					?
				)
				''', t)
		except sqlite3.OperationalError:
			print("Unable to insert CD '%s' into database") % name
			return

		self.con.commit()

	def getArtists(self):
		"""
		Fetch list of Artists from database
		"""
		artists = []
		for row in self.c.execute("SELECT * FROM Artists"):
			artists.append(Artist(row))

		return artists

	def getCDs(self):
		"""
		Fetch list of CDs from database
		"""
		cds = []
		for row in self.c.execute("SELECT * FROM CDs"):
			cds.append(CD(row))

		return cds

	def getArtistByID(self, id):
		"""
		Fetch Artist from database with matching id
		"""
		t = (id,)
		self.c.execute("SELECT * FROM Artists WHERE ID=?", t)
		result = self.c.fetchone()
		return Artist(result)

	def getArtistByName(self, name):
		"""
		Fetch Artist from database with matching name
		"""
		t = (name,)
		self.c.execute("SELECT * FROM Artists WHERE Name=?", t)
		result = self.c.fetchone()
		return Artist(result)

	def getCDByID(self, id):
		"""
		Fetch CD from database with matching id
		"""
		t = (id,)
		self.c.execute("SELECT * FROM CDs WHERE ID=?", t)
		result = self.c.fetchone()
		return CD(result)

	def getCDsByArtistName(self, artist):
		"""
		Fetch CDs from database with matching artist name
		"""
		artist_id = self.getArtistByName(artist).id
		t = (artist_id,)
		cds = []
		for row in self.c.execute("SELECT * FROM CDs WHERE Artist=?", t):
			cds.append(CD(row))
		return cds

