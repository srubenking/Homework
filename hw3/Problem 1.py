#__author__ = scweiser and srubenking

import json
import re
#importing json and regular expressions modules

cmDict = "cmdict7a.json"
f = open(cmDict,"r")
dict = json.load(f)
f.close()
del f
#this opens and reads the cm dictionary


def tokenizeFile(path):
    """
    This reads a json file, and separates the words into tokens in a list.
    arguments: a file path
    returns: a list of the tokenized words.
    """
    words = [] #creates an empty list for tokens
    f = open(path, "r")  #opens and reads the file
    for line in f:
        line_words = re.findall(r"[A-Za-z-']+", line.lower()) #for each line, finds all words in the line with lower or uppercase letters, including apostrophes and dashes.
        words.extend(line_words) #adds the words from each line to list to be returned
    return words

def phonemeList(list):
    """
    This takes a list of words, and returns their phonemic representation.
    arguments: a list of words
    returns: a list of phonemic expressions for words, each contained within a list.
    """
    phonemeListOut = [] #the list to be returned
    for word in list:
        phonemeRep = None #sets default phonemic expression to nothing
        if word in dict:
            phonemeRep = dict[word][0] #if the word is in cmdict, this overwrites phonemeRep with its phonemic representation.
        else:
            pass
        if phonemeRep != None:
            phonemeListOut.append(phonemeRep) #this only adds the word to the phoneme list if it has a phonemic representation.
    return phonemeListOut

def fileToPhoneme(path):
    """
    This is the main function that runs the other two functions
    arguments: a file path
    returns: a list of the phonemic expressions for every word in the file.
    """
    fileTokens = tokenizeFile(path)
    return phonemeList(fileTokens)

mtnHs = "./SampleTexts/mountainhouses.txt"

print fileToPhoneme(mtnHs) #this prints the phonemic representation for the mountainhouses text.
