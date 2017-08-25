# csv = Output file
# mFile = input file

# Open and close the output file to remove all text in it
with open('asd.csv', 'w') as csv: pass

# Actual code to convert text file into csv file
with open('asd.txt', 'r') as mFile:
    with open('asd.csv', 'w') as csv:
        # Reads line by line.
        for line in mFile:
            try:
                # Notes indexes
                idx_country = str(line).index('Country')
                idx_count = str(line).index('Req')
                idx_suc = str(line).index('Succ')

                # Creates a string containing commas at specific places. Writes to output file
                csv.write(line[4:idx_country - 1] + ',' + line[idx_country + 9:idx_count - 1] + ',' + line[idx_count + 15:idx_suc - 1])

                # Adds \n at the end of each line. Writes to output file
                csv.write('\n')
            except: pass
