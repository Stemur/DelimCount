#!/usr/bin/python

import sys, getopt
import locale

locale.setlocale(locale.LC_NUMERIC, 'en_US')

# Global Variables
filesize = 0
countonly = False

def processfile(inputfile):
	global countonly
	global filesize
	lineno = 1
	try:
		with open(inputfile, 'r') as f:
			delimcount = 0
			read_data = f.readline()
			while read_data:
				delimcount = read_data.count(',')
				filesize += len(read_data)
				outputdata(read_data, delimcount, lineno)
				lineno += 1
				read_data = f.readline()
	except IOError as e:
		print 'Error {0} : {1}'.format(e.errno, e.strerror)
		sys.exit(2)
	f.close()

def outputdata(linedata, delcount, lineno):
	global countonly
	print 'Line : {:<5}'.format(lineno), # % (lineno),
	if countonly == False:
		print ' {:<5}'.format(delcount),
		print linedata.rstrip()
	else:
		print ' Delimiter Count : %i ' % (delcount)

def main(argv):
	global countonly
	inputfile = ''
	usgstr = 'Correct useage is: delimcount.py [-c] -i <inputfile>'
	try:
		opts, args = getopt.getopt(argv,"hci:",['ifile='])
	except getopt.GetoptError:
		print usgstr
		sys.exit(2)
	if len(opts) == 0:
		print "No options supplied. %s" % usgstr
		sys.exit()
	for opt, arg in opts:
		if opt == '-i':
			inputfile = arg
		elif opt == '-h':
			print "delimcount.py [-c] -i <inputfile>"
			sys.exit()
		elif opt == '-c':
			print 'Displaying delimiter counts for each line only.'
			countonly = True
	if len(inputfile) == 0:
		print "No input file name supplied. %s" % usgstr
		sys.exit()
	print 'File Name : %s' % inputfile
	processfile(inputfile)
	print 'File size (bytes) : ' + locale.format('%i', filesize, grouping = True)

if __name__ == "__main__":
	main(sys.argv[1:])
