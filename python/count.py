intro=input("Give your Introduction")
print(intro) 
charactercount=0
wordcount=1

for i in intro:
    charactercount = charactercount + 1
    if(i==' '):
        wordcount = wordcount + 1

print("number of word in string")        
print(wordcount + 1)
print("number of character in string")
print(charactercount)

    
