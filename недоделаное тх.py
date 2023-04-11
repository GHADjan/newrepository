


sent = "Singing in the rain and playin in the rain are two entirely different situations but both can be good "

wordlist = sent.split()
worddict = {}


for word in wordlist:
    if word in worddict:
        worddict[word] += 1
    else:
        worddict[word] = 1


print(worddict)
print(worddict.items())



