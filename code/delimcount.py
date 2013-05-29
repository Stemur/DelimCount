#!/usr/bin/python

import sys, getopt
import locale

locale.setlocale(locale.LC_NUMERIC, 'en_US')

# Global Variables
filesize = 0

def processfile(inputfile):
	global filesize
	lineno = 1
	try:
		with open(inputfile, 'r') as f:
			delimcount = 0
			read_data = f.readline()
			while read_data:
				if lineno == 1:
					print 'Ct Line Data'
				delimcount = read_data.count(',')
				filesize += len(read_data)
				outputdata(read_data, delimcount)
				lineno += 1
				read_data = f.readline()
	except IOError as e:
		print 'Error {0} : {1}'.format(e.errno, e.strerror)
		sys.exit(2)
	f.close()

def outputdata(linedata, delcount):
	print '%i ' % (delcount),
	print linedata.rstrip()
		
def main(argv):
	inputfile = ''
	usgstr = 'Correct useage is: delimcount.py -i <inputfile>'
	try:
		opts, args = getopt.getopt(argv,"i:",['ifile='])
	except getopt.GetoptError:
		print usgstr
		sys.exit(2)
	if len(opts) == 0:
		print "No options supplied. %s" % usgstr
		sys.exit()
	for opt, arg in opts:
		if opt == '-i':
			inputfile = arg
	if len(inputfile) == 0:
		print "No input file name supplied. %s" & usgstr
		sys.exit()
	print 'File Name : %s' % inputfile
	processfile(inputfile)
	print 'File size (bytes) : ' + locale.format('%i', filesize, grouping = True)

if __name__ == "__main__":
	main(sys.argv[1:])
