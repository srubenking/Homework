#__author__ = scweiser and srubenking

import json
#importing json to read json files

cmDict = "cmdict7a.json"
f = open(cmDict,"r")
dict = json.load(f)
f.close()
#this opens and reads the cm dictionary

def phonemeList(list):
    """
    This takes a list of words, and returns their phonemic representation.
    arguments: a list of words
    returns: a list of phonemic expressions for words, each contained within a list.
    """
    phonemeListOut = []#the list to be returned
    for word in list:
        phonemeRep = None #sets default phonemic expression to nothing
        if word in dict:
            phonemeRep = dict[word][0] #if the word is in cmdict, this overwrites phonemeRep with its phonemic representation.
        else:
            pass
        if phonemeRep != None:
            phonemeListOut.append(phonemeRep) #this only adds the word to the phoneme list if it has a phonemic representation.
    return phonemeListOut



def dictCount(list):
    """
    This takes a list of phonemic representations of words, and creates a dictionary counting how many times phonemes appear next to each other.
    arguments: a list of lists
    returns: a dictionary.  Each key of the dictionary is a phoneme.  the value is a dictionary of the phonemes that appear after it, and the number of times they appear in this way.
    """
    countDict = {} #empty list to be returned
    for word in list:
        for phon in range(0,len(word)-1): #loops through each phoneme in the word, except the last phoneme
            #!!! phon is a confusing name, because it's a number
            #!!! instead, let it be index or i, and up here, set some variables:
            #!!! phon = word[i]
            #!!! next = word[i+1]
            #!!! Then you can make the code below more readable
            if word[phon] not in countDict:
                countDict[word[phon]] = {word[phon+1]: 1} #creates a new dictionary entry if there is none for that phoneme
            elif word[phon+1] in countDict[word[phon]]:
                countDict[word[phon]][word[phon+1]] += 1 #increases the count of the sub-dictionary if there is one
            else:
                countDict[word[phon]][word[phon+1]] = 1 #creates a new sub-dictionary entry if there is none for that pair
    return countDict
    #!!! Otherwise, this is an excellent solution.


woodchuckStr = "how much wood could a woodchuck chuck if a woodchuck could chuck wood"
woodchuckLst = woodchuckStr.split(" ") #creates list of words
phonemes =  phonemeList(woodchuckLst) #creates list of list of phonemes
print dictCount(phonemes) #prints the counting dictionary




