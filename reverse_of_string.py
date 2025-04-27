word=input("enter the word to get reverse:")
new_word=""
for char in word:
    new_word=char+new_word
print (f"reverse word of {word} ={new_word}")