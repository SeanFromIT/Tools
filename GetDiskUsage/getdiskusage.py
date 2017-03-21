#!/usr/bin/python

#https://github.com/SeanFromIT/Tools.git

import sys, getopt, os, json

def usage():
	print "getdiskusage.py /tmp"

#innerfiles = {}
innerfiles = []

#Input sanity checks

try:
	opts, args = getopt.getopt(sys.argv[1:], 'h', ["help"])
except getopt.GetoptError as e:
	print e
	print "Try:"
	usage()
	sys.exit(2)

for opt, arg in opts:
	if opt in ('-h', '--help'):
		usage()
		sys.exit(2)

arguments = len(sys.argv)

if arguments < 2:
	print "Please include a mountpoint. E.g."
	usage()
	sys.exit(2)
elif arguments > 2:
	print "Please only include one mountpoint. If there is a space in your mountpoint, try encasing it in quotes. E.g. getdiskusage.py '/path/to/spaced folder'"
	sys.exit(2)

mountpoint = sys.argv[1]

if not mountpoint.startswith("/"):
	print "A mountpoint must start with /. E.g."
	usage()
	sys.exit(2)
elif not os.path.isdir(mountpoint):
	print mountpoint + " is not a valid mountpoint. Try getdiskusage.py -h for help."
	sys.exit(2)

#Sanity check passed, now recursively itemize files

for subdir, dirs, files in os.walk(mountpoint):

	#Catch directory permission errors
	for dirname in dirs:
		dir = os.path.join(subdir, dirname)
		if not os.access(dir, os.R_OK):
			print dir + " files and subdirs will not be parsed due to permissions error."

	for file in files:

		#Get filepath
		filepath = subdir + os.sep + file

		#Get size for filepath
		try:
			#innerfiles[filepath] = os.path.getsize(filepath)
			innerfiles.extend((filepath, os.path.getsize(filepath)))
		except OSError as e:
			print filepath + " will not be returned due to error:"
			print e

#Format output
output = {}
output["files"] = innerfiles

print(json.dumps(output,indent=2))

sys.exit()