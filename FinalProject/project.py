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
    return re.split(r'(\w+)',s)

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
            if re.match(abc, word): #adds the non-matched item to the notInDict list if it is a word (rather than space or punctuation)
                notInDict.append(word)
    if choice == 'T':
        return u''.join(pigList) #returns the list, joined into a string
    else:
        return u'\n'.join(notInDict)
if __name__ == "__main__":
    global notInDict
    notInDict = [] #initializes a list to hold words that weren't in the dictionary
    choice = raw_input('Do you want to translate (T) or see the list of exceptions (E)? ')
    f = open('twain','r')

    lines = [line.decode('utf-8').strip() for line in file.readlines(f)]
    for line in lines: #demonstrates the program for the first 10 lines of 'twain'
        print pigLatin(line)