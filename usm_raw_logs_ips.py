import sys
name_of_file = str(sys.argv[1])
mString = ''
# try:
with open(name_of_file, 'r') as mFile:
    for line in mFile:
        mString = mString + ' ip=' + line.rstrip('\n') + ' or'
mString = mString.lstrip(' ')
mString = mString.rstrip(' or')
with open(name_of_file+'done', 'w') as mFile: mFile.write(mString)
