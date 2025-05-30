#Accept a line of text that counts total no. of vowels,consonants,digits and ther special characters

st=input('Enter a line of text : ')
c1=0
c2=0
c3=0
c4=0
st=st.lower()  #makes every alphabet in lower case
for var in st:
    #if var in 'aeiou':
    if var=='a' or var=='e' or var=='i' or var=='o' or var=='u':
        c1+=1
    #if 'a'<=var<='z' and var not in 'aeiou':
    elif var!='a' and var!='e' and var!='i' and var!='o' and var!='u' and 'a'<=var<='z':
        c2+=1
    elif '0'<=var<='9':
        c3+=1
    else:
        c4+=1
print('no. of vowels is ',c1)
print('no. of consonents is ',c2)
print('no. of digits is ',c3)        
print('no. of special characters is ',c4)