#Creation of a file exclusively and appending contents to that created file

import os

dir_file='S:\\Documents\\Github\\Computational-Physics-UG\\Introductory Techniques in Python\\File Handling\\filecreate_x.txt'
buffer=4095                                           #Here buffer denoting the memory location where the set of characters are stored to write to the opened file

if not os.path.exists(dir_file):    
    #Creation of file object
    with open(dir_file, 'x') as fp:                   #Exclusive create mode “x”
        print("File created for 1st and last time")   #A new file with same name cant be further created in same location
        fp.write('Create Mode')
else:
    with open(dir_file, 'a') as fp:                   #Append mode “a”
        str='Welcome to python\n'
        fp.write(str)
        fp.close()                                    #After closing a file, it releases all the corresponding resources
        print("File already exists, content appended")

