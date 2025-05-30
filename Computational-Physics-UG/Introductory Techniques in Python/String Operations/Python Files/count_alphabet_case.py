#Accept a string and count the total number of lower case and upper case alphabets

st=input("Enter a string: ")
c1=0  # Counter for uppercase letters
c2=0  # Counter for lowercase letters

#Iterate through each character in the string
for char in st:
    if 'A'<=char<='Z':    #Check if the character is uppercase (ASCII range for uppercase letters)
        c1 += 1
    elif 'a'<=char<='z':  # Check if the character is lowercase (ASCII range for lowercase letters)
        c2 += 1

print("Number of uppercase letters is :", c1)
print("Number of lowercase letters is :", c2)
