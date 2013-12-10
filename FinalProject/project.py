# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import re
import json

f = open('cmdict7a.json','r') #loads the cmdict arpabet dictionary
dictionary = json.load(f)
f.close()

arpaDict = {'P':u'p', #arpabet to IPA conversion dictionary
           'T':u't',
           'K':u'k',
           'B':u'b',
           'D':u'd',
           'G':u'g',
           'L':u'l',
           'M':u'm',
           'N':u'n',
           'NG':u'ŋ',
           'F':u'f',
           'V':u'v',
           'TH':u'θ',
           'DH':u'ð',
           'S':u's',
           'Z':u'z',
           'SH':u'ʃ',
           'ZH':u'ʒ',
           'W':u'w',
           'R':u'r',
           'Y':u'j',
           'HH':u'h',
           'CH':u'tʃ',
           'JH':u'dʒ',
           'IY':u'i',
           'IH':u'ɪ',
           'EY':u'eɪ',
           'EH':u'ɛ',
           'AE':u'æ',
           'AA':u'a',
           'AO':u'ɔ',
           'OW':u'oʊ',
           'UH':u'ʊ',
           'UW':u'u',
           'ER':u'ɚ',
           'AH':u'ʌ',
           'AY':u'aɪ',
           'AW':u'aʊ',
           'OY':u'ɔɪ',
           'AX':u'ə'}

def splitString(s):
    '''
    takes a string and separates on word boundaries, creating a list of words, spaces and punctuation

    Args:
        s: a sentence
    '''
    splitRE = re.compile(u'''
                        ([\.](?!\w)|   #periods if they aren't followed by a word character
                        [\s(),\-:;"﻿]|   #punctuation to always split on
                        \'(?!\w)      #apostrophes if they don't have a word character after them
                        )''',re.VERBOSE)
    return splitRE.split(s)

def pigLatinWord(w):
    '''
	takes word w, finds its arpabet phonemic representation, converts it into IPA and translates into Pig Latin

    Args:
		w: a word that is in cmdict

    Returns:
        word w translated into Pig Latin
	'''
    vowels = [u'ɪ',u'e',u'u',u'æ',u'i',u'ɛ',u'ʊ',u'o',u'ɔ',u'ɑ',u'a',u'ɚ',u'ʌ',u'ə'] #all English IPA vowels
    arpaWord = dictionary[w][0] #finds the first pronunciation of w in the arpabet dictionary
    ipaPhonemes = []

    for phon in arpaWord: #converts arpabet phonemes into IPA
        ipaPhonemes.append(arpaDict[phon])
    ipaWord = ''.join(ipaPhonemes) #joins the IPA phoneme list into one word

    if ipaWord[0] in vowels: #if it starts with a vowel, appends a suffix
        if ipaWord[0] == u'ɪ':
            return ipaWord + u'wej' #'-wej' suffix if the word starts with an 'ɪ' sound
        else:
            return ipaWord + u'ej' #'-ej' suffix if the word starts with any other vowel sound
    else:
        for n in range(0,len(ipaWord)): #goes through each letter in the word and stops at the first vowel
            if ipaWord[n] in vowels:
                return ipaWord[n:] + ipaWord[0:n] + u'ej' #after it finds a vowel, moves the onset to word final position then appends 'ej'

def pigLatin(text):
    '''
	takes string 'text' and runs pigLatinWord on each word if they are in cmdict

    Args:
		text: a string

    Returns:
        the string translated into Pig Latin
    '''
    splitText = splitString(text.lower()) #splits the string into a list of words, spaces and punctuation
    pigList = []
    abc = re.compile(r'[a-zA-Z]\w') #regular expression to check if something is a word and not space or punctuation

    for word in splitText: #runs pigLatinWord for each word in the list that is in cmdict
        if word in dictionary:
            pigList.append(pigLatinWord(word))
        else:
            pigList.append(word.upper())
            if re.match(abc, word): #adds the untranslatable item to the notInDict list if it is a word (rather than space or punctuation)
                if word not in notInDict:
                    notInDict.append(word)
    return u''.join(pigList) #returns the list, joined into a string

def pigFileRead(filename,n):
    '''
    takes a string that is a filename or path to a filename and an int for the number of lines to print

    Args:
        filename: a string
        n: an int

    Returns:
        nothing, it runs pigLatin on each line for the number of lines specified by arg n
    '''
    f = open(filename,'r')

    lines = [line.decode('utf-8').strip() for line in file.readlines(f)] #decodes the lines to unicode and splits each line of the file into a list
    f.close()
    for line in lines[0:n]: #runs pigLatin for the first n lines of f
        print pigLatin(line)
    print '\n---------------------------------------------------------------------\n'
    choice = raw_input("Would you like to the see the words that weren't translated (y/n)? ")
    if choice in ['Y','y']: #if the user says yes to the prompt, prints out the untranslated words with spaces in between
        for item in notInDict:
            if item is not notInDict[-1]:
                print item + ',',
            else:
                print item

if __name__ == "__main__":
    global notInDict
    notInDict = [] #initializes a list to hold words that weren't in the dictionary
    fName = raw_input('Enter the path to the file you would like to load: ')
    lineNum = int(input('Now enter the number of lines you would like to translate: '))
    pigFileRead(fName,lineNum) #uses the user input to translate the desired file to the number of lines the user desires
