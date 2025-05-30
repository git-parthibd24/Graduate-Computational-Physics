#Creation of a file and appending/reading contents to that created file

buffer=4095

#Creation of file object
fp=open('S:\\Documents\\Github\\Computational-Physics-UG\\Introductory Techniques in Python\\File Handling\\filecreate_a+.txt','a+',buffer)   #Append mode “a+”                            

#Writing to the file (This file cant be read)       
str='Welcome to python\n'
for i in range(4):
    fp.write(str)

print("Content updated and will be again appended on next execution of script")
print()
print('Current pointer offset :',fp.tell())
print()            #current pointer location

fp.seek(0,0)        #moves the pointer to the beggining of file as it was moved to last after creating the file using seek(offset,whence) where seek is position of pointer and whence is 0,1,2 indicating start from beginning, start from current offset position, start relative to end of the file respectively
str=fp.read()
print('The file is read as :')
print(str)

fp.close()                              #After closing a file, it releases all the corresponding resources