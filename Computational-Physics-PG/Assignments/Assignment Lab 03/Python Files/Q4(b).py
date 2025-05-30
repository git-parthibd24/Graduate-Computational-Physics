#Question 4(b) 
#Count how many times a certain string appears in another string. For example, the function returns 3 when called with the DNA string 'ACGTTACGGAACG' and the substring 'ACG'

def count_pairs(main_string,sub_string):
    count=0
    n=len(sub_string)
    
    # Extract successive substrings from the main string and compare them to the substring
    for i in range(len(main_string)-n+1):  
        if main_string[i]==sub_string[0]:  
            if main_string[i+1:i+n]==sub_string[1:]:  # Check the rest of the substring excluding 1st character
                count+=1  
    return count

dna=input('Enter the DNA sequence : ')
subdna=input('Enter the pair to be counted in the DNA sequence : ')
result=count_pairs(dna,subdna)
#print(f"The substring {subdna} appears {result} times in the main string")
print("The substring " + subdna + " appears " + str(result) + " times in the main string") #string concatenation i.e adding strings together