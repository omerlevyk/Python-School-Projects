def max_chr(word):
    if len(word) == 1:
        #print(word)
        return(word)
    elif ord(word[0]) - ord(word[-1]) > 0:
        return(max_chr(word[:-1]))
        #print(word)
        #return(word)
    else:
        return(max_chr(word[1:]))
        #print(word)
        #return(word)

word = input("")
#max_chr(word)
print(max_chr(word))
#print(word)
