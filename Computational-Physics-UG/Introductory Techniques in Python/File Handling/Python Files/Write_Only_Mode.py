#Creation of a file and writting contents to that created file

buffer=4095

#Creation of file object
fp=open('S:\\Documents\\Github\\Computational-Physics-UG\\Introductory Techniques in Python\\File Handling\\filecreate_w.txt','w',buffer)   #Append mode “w”                            

lorem_ipsum_lines=["Lorem ipsum dolor sit amet,","consectetur adipiscing elit.","Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.","Ut enim ad minim veniam,","quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.","Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.","Excepteur sint occaecat cupidatat non proident,","sunt in culpa qui officia deserunt mollit anim id est laborum."]


#Writing to the file (This file cant be read)    

for line in lorem_ipsum_lines:
        fp.write(line + '\n')
fp.close()                              #After closing a file, it releases all the corresponding resources
print("Content Appended and will be overwritten on next execution of the script on same file")