#Reading contents from a file

buffer=4095

#Creation of file object
fp=open('S:\\Documents\\Github\\Computational-Physics-UG\\Introductory Techniques in Python\\File Handling\\filecreate_w.txt','r',buffer)   #Append mode “r”                            

#Reading the file (This file cant be written)
   
str1=fp.read()
print("Content Read as : ")
print(str1)
print()

fp.seek(0)                    #Bringing the pointer/file offset to beginning of file again

str1=fp.read(7)
print('The 1st 7 characters is read as : ')
print(str1)
print()

fp.seek(0)

str2=fp.readline()
print('The 1st line is read as : ')
print(str2)
print()

fp.seek(0)

str3=fp.readline(5)
print('The 1st 5 characters is read as : ')
print(str3)
print()

fp.seek(0)

str3=fp.readlines()          #Returns a list of all lines as strings
print("Content Read as : ")
print(str3)