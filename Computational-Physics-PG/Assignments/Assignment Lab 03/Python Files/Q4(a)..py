#Question 4(a) 
#Write a function count_pairs(dna,pair) that returns the number of occurrences of a pair of characters (pair) in a DNA string (dna). For example, calling the function with dna as 'ACT-GCTATCCATT' and pair as 'AT' will return 2


def count_pairs(dna,pair):
    count=0
    n=len(pair)
    
    # Extract successive pairs of characters from the main string and compare them to the substring
    for i in range(len(dna)-1):           # Stop at len(dna)-1 to avoid index out of range
        if dna[i:i+n]==pair:  
            count+=1              
    return count

dna=input('Enter the DNA sequence : ')
pair=input('Enter the pair to be counted in the DNA sequence : ')
result=count_pairs(dna,pair)
print(f"The pair {pair} appears {result} times in the main string")
