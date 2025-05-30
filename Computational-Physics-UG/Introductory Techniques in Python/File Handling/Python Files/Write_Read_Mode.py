#Creation of a file and writting/reading contents to that created file

buffer=4095

#Creation of file object
fp=open('S:\\Documents\\Github\\Computational-Physics-UG\\Introductory Techniques in Python\\File Handling\\filecreate_w+.txt','w+',buffer)   #Append mode “w+ or r+”                            

lorem_ipsum_lines=["Lorem ipsum dolor sit amet,","consectetur adipiscing elit.","Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.","Ut enim ad minim veniam,","quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.","Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.","Excepteur sint occaecat cupidatat non proident,","sunt in culpa qui officia deserunt mollit anim id est laborum."]


#Writing to the file    

for line in lorem_ipsum_lines:
        fp.write(line + '\n')

print("Content Appended and will be overwritten on next execution of the script on same file")
print()
print('Current pointer offset :',fp.tell())
print()             #current pointer location

fp.seek(0,0)        #moves the pointer to the beggining of file as it was moved to last after creating the file using seek(offset,whence) where seek is position of pointer and whence is 0,1,2 indicating start from beginning, start from current offset position, start relative to end of the file respectively
str=fp.read()
print('The file is read as :')
print(str)

fp.close()          #After closing a file, it releases all the corresponding resources