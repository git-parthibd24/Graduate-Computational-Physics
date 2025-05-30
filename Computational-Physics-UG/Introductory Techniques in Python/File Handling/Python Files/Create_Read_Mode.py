#Creation/Reading of a file exclusively and appending contents to that created file

import os

dir_file='S:\\Documents\\Github\\Computational-Physics-UG\\Introductory Techniques in Python\\File Handling\\filecreate_x+.txt'
buffer=4095                                            #Here buffer denoting the memory location where the set of characters are stored to write to the opened file

if not os.path.exists(dir_file):    
    #Creation of file object
    with open(dir_file, 'x+') as fp:                   #Exclusive create mode “x+”
        print("File created for 1st and last time")    #A new file with same name cant be further created in same location
        fp.write('Create Mode')
        print()
        print('Current pointer offset :',fp.tell())
        print()                                        #current pointer location

        fp.seek(0,0)                                   #moves the pointer to the beggining of file as it was moved to last after creating the file using seek(offset,whence) where seek is position of pointer and whence is 0,1,2 indicating start from beginning, start from current offset position, start relative to end of the file respectively
        str=fp.read()
        print('The file is read as :')
        print(str)

        fp.close()
else:
    with open(dir_file, 'a') as fp:                   #Append mode “a”
        str='Welcome to python\n'
        fp.write(str)
        fp.close()                                    #After closing a file, it releases all the corresponding resources
        print("File already exists, content appended")

