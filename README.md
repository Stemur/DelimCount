# DelimCount
---
Python script to read an ascii file and count the number of comma delimiters on each line.

Usage:

delimcount [-c] -i <FileName>

    Parameters:
    
        -c : Optional - Return a count on each line.
        -i : Required - Name of file to be inspected.
        -d : Optional - The delimiter character to be counted.

e.g. delimcount -c -i testfile.txt -d ,

#### Notes:
The -d cli parameter - This may require an escape character to work. 
    e.g. for a pipe delimiter, you would need to enter \\|
    
The default delimiter is the comma.
