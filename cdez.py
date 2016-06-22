#!/usr/bin/python

import sqlite3
import os.path

from artist import Artist
from cd import CD

VERSION = "0.0.2"
DB_PATH = "cdez.db"

print("CDez v%s") % (VERSION)

def create_db(db_path):
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


# check for existence of db
if not(os.path.isfile(DB_PATH)):
	print("Database DNE; creating...")
	create_db(DB_PATH)

# db existence asserted, onward...
con = sqlite3.connect("cdez.db")
c = con.cursor()

def createArtist(name):
	"""
	Insert new Artist into database
	"""
	t = (name,)
	try:
		c.execute('''INSERT INTO Artists
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

	con.commit()

def createCD(artist, name, box, location):
	"""
	Insert new CD into database
	"""
	t = (artist, name, box, location,)
	try:
		c.execute('''INSERT INTO CDs
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

	con.commit()

def getArtists():
	"""
	Fetch list of Artists from database
	"""
	artists = []
	for row in c.execute("SELECT * FROM Artists"):
		artists.append(Artist(row))

	return artists

def getCDs():
	"""
	Fetch list of CDs from database
	"""
	cds = []
	for row in c.execute("SELECT * FROM CDs"):
		cds.append(CD(row))

	return cds

def getArtistByID(id):
	"""
	Fetch Artist from database with matching id
	"""
	t = (id,)
	c.execute("SELECT * FROM Artists WHERE ID=?", t)
	result = c.fetchone()
	return Artist(result)

def getCDByID(id):
	"""
	Fetch CD from database with matching id
	"""
	t = (id,)
	c.execute("SELECT * FROM CDs WHERE ID=?", t)
	result = c.fetchone()
	return CD(result)
