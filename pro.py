filename=input("enter file name")
searchstring=input("enter word you want to search")
f=open(filename)
filelines=f.readlines()
found=False 
counter=0
for line in filelines:
    words=line.split()
    for word in words: 
        if word==searchstring:
            found=True
            counter=counter+1
if  found==True:
    print("the word is present ", counter," times")
else:
    print("word is not found")