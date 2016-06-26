#!/usr/bin/python

import os.path
import argparse

from database import Database

VERSION = "0.0.3"
DB_PATH = "cdez.db"


# check for existence of db
if not(os.path.isfile(DB_PATH)):
	print("Database DNE; creating...")
	Database.create_db(DB_PATH)

# db existence asserted, onward...
# argparse time
parser = argparse.ArgumentParser(description="Small tool to aid in managing optical media collection")
parser.add_argument("op", help="operation to be performed", type=str)
#parser.add_argument("-v", "--version", action="store_true", help="print version information")

def version():
	print("CDez v%s") % VERSION

def op_add_entry():
	print("add")

def op_list_entries():
	print("list")

def op_remove_entry():
	print("remove")

args = parser.parse_args()
action = {
	"add": op_add_entry,
	"list": op_list_entries,
	"remove": op_remove_entry,
}

print("CDez v%s") % (VERSION)

try:
	action[args.op]()
except KeyError:
	print("Operation not recognized: '%s'") % args.op
	exit()
