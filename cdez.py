#!/usr/bin/python

import os.path
import argparse

from database import Database

VERSION = "0.0.4"
DB_PATH = "cdez.db"


# check for existence of db
if not(os.path.isfile(DB_PATH)):
	print("Database DNE; creating...")
	Database.create_db(DB_PATH)

# db existence asserted, onward...
# argparse time
parser = argparse.ArgumentParser(description="Small tool to aid in managing optical media collection")
parser.add_argument("op", help="operation to be performed", type=str)
parser.add_argument("--artist", help="(for add, list) perform operation on artist", action="store_true")
parser.add_argument("--cd", help="(for add, list) perform operation on cd", action="store_true")
parser.add_argument("--byid", help="(for search) to search by ID", action="store_true")
parser.add_argument("--byname", help="(for search) to search by Name", action="store_true")
parser.add_argument("--byartist", help="(for search) to search by Artist", action="store_true")
#parser.add_argument("-v", "--version", action="store_true", help="print version information")

def op_exit():
	exit(0)

def op_add_artist():
	print("")
	print("Add Artist")
	print("----------")
	name = raw_input("Name: ")
	
	db = Database()
	db.createArtist(name)

	print("Artist '%s' added.") % (name)

def op_add_cd():
	print("")
	print("Add CD")
	print("------")

def op_add_entry():
	if (args.artist):
		op_add_artist()
	else:
		op_add_cd()

def op_list_artists():
	print("Artists: ")
	for a in db.getArtists():
		print("%i\t%s") % (a.id, a.name)

def op_list_cds():
	for c in db.getCDs():
		print("%i\t%s\t\t%s") % (c.id, db.getArtistByID(c.artist).name, c.name)

def op_remove_entry():
	print("remove")

def op_search():
	db = Database()
	if (args.artist):
		if (args.byid):
			a = db.getArtistByID(raw_input("Enter ID: "))
			print("(%i) %s") % (a.id, a.name)
		else:
			a = db.getArtistByName(raw_input("Enter Name: "))
			print("%i (%s)") % (a.id, a.name)
	else:
		if (args.byid):
			c = db.getCDByID(raw_input("Enter ID: "))
			print(c)
		else:
			if (args.byartist):
				cds = db.getCDsByArtistName(raw_input("Enter Artist: "))
				for c in cds:
					print(c)


args = parser.parse_args()
action = {
	"add": op_add_entry,
	"search": op_search,
	"listcds": op_list_cds,
	"listartists": op_list_artists,
	"remove": op_remove_entry,
}

print("CDez v%s") % (VERSION)

try:
	action[args.op]()
except KeyError:
	print("Operation not recognized: '%s'") % args.op
	exit()
