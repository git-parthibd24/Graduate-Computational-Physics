#Creation of a file and appending contents to that created file

buffer=4095

#Creation of file object
fp=open('S:\\Documents\\Github\\Computational-Physics-UG\\Introductory Techniques in Python\\File Handling\\filecreate_a.txt','a',buffer)   #Append mode “a”                            

#Writing to the file (This file cant be read)       
str='Welcome to python\n'
for i in range(4):
    fp.write(str)
fp.close()                              #After closing a file, it releases all the corresponding resources
print("Content updated and will be again appended on next execution of script")
