word=input("enter a sentence:")
count=0
for char in word:
    if(char!=" "):
        count+=1
print(f"There are {count} char in the given sentence = { word}")