#!/usr/bin/python

import sys
import locale
import argparse

locale.setlocale(locale.LC_NUMERIC, 'en_US')


def processfile(inputfile, countonly, delim):
    filesize = 0
    lineno = 1
    try:
        with open(inputfile, 'r') as f:
            read_data = f.readline()
            print('File Name : %s' % inputfile)
            while read_data:
                delimcount = read_data.count(delim)
                filesize += len(read_data)
                outputdata(read_data, delimcount, lineno, countonly)
                lineno += 1
                read_data = f.readline()
    except IOError as e:
        print('Error {0} : {1}'.format(e.errno, e.strerror))
        sys.exit(2)
    f.close()
    print('File size (bytes) : ' + locale.format_string('%i', filesize, grouping=True))


def outputdata(linedata, delcount, lineno, countonly):
    print('Line : {:<5}'.format(lineno), end='')
    if not countonly:
        print(' {:<5}'.format(delcount), end='')
        print(linedata.rstrip())
    else:
        print(' Delimiter Count : %i ' % delcount)


def main():
    # Argument Parser
    arg_parser = argparse.ArgumentParser(prog='delimcount',
                                         usage='%(prog)s [options] -i filename',
                                         description='count the number of delimiters on each line in a file')
    arg_parser.add_argument('-c', '--count', action='store_true',
                            dest='countonly',
                            help='display delimiter counts on each line',
                            required=False)
    arg_parser.add_argument('-i', '--input', action='store',
                            metavar='[file name]',
                            dest='inputfile',
                            type=str,
                            help='the name of the file to be inspected',
                            required=True)
    arg_parser.add_argument('-d', action='store',
                            metavar='[delimiter]',
                            dest='delimvalue',
                            default=',',
                            type=str,
                            help='the delimiter character to be counted (may need to be escaped e.g.\|)')

    args = arg_parser.parse_args()
    processfile(args.inputfile, args.countonly, args.delimvalue)


if __name__ == "__main__":
    main()
