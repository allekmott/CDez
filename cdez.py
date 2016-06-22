#!/usr/bin/python

import sqlite3
import os.path

VERSION = "0.0.1"
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
				ID INT NOT NULL PRIMARY KEY,
				Artist INT NOT NULL,
				Name TEXT NOT NULL,
				Box INT NOT NULL,
				Location TEXT NOT NULL
			)''')
	except sqlite3.OperationalError:
		print("Unable to create table 'CDs'")

	try:
		# write command to create Artists
		c.execute('''CREATE TABLE Artists
			(
				ID INT NOT NULL PRIMARY KEY,
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

