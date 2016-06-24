#!/usr/bin/python

import os.path

from database import Database

VERSION = "0.0.3"
DB_PATH = "cdez.db"

print("CDez v%s") % (VERSION)


# check for existence of db
if not(os.path.isfile(DB_PATH)):
	print("Database DNE; creating...")
	Database.create_db(DB_PATH)

# db existence asserted, onward...
