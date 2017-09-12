# For all files in a directory
import os
for file_name in os.listdir('rules'):
    # Output file
    with open('out.txt', 'w') as out:
        # Input Directory = 'rules/'
        with open('rules/' + file_name, 'r') as file:
            for line in file:
                # Search for a keyword
                if 'ETPRO' in line: out.write(line + '\n')
