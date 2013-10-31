#__author__ = scweiser and srubenking

import json
import re


cmDict = "cmdict7a.json"
f = open(cmDict,"r")
dictionary = json.load(f)
f.close()
del f
#reads the json phoneme dictionary


class FrequencyTable(object):

    def __init__(self,path):
        """
        defines variables and functions for the FrequencyTable class.
        Takes a path as an argument
        """
        self.path = str(path)
        self.tokens = self.tokenize()
        self.phonemes = self.phonemeList()
        self.frequency = self.frequencyDict()


    def tokenize(self):
        """
        This reads a json file, and separates the words into tokens in a list.
        arguments: a file path
        returns: a list of the tokenized words.
        """
        words = []
        f = open(self.path, "r")
        for line in f:
            line_words = re.findall(r"[A-Za-z-']+", line.lower())
            words.extend(line_words)
        return words

    def phonemeList(self):
        """
        This takes a list of words, and returns their phonemic representation.
        arguments: a list of words
        returns: a list of phonemic expressions for words, each contained within a list.
        """
        phonemeListOut = []
        for word in self.tokens:
            phonemeRep = None
            if word in dictionary:
                phonemeRep = dictionary[word][0]
            if phonemeRep != None:
                phonemeListOut.append(phonemeRep)
        return phonemeListOut

    def frequencyDict(self):
        """
        This takes a list of phonemic representations of words, and creates a dictionary counting how many times phonemes appear next to each other.
        arguments: a list of lists
        returns: a dictionary.  Each key of the dictionary is a phoneme.  the value is a dictionary of the phonemes that appear after it, and the number of times they appear in this way.
        """
        countDict = {}
        for word in self.phonemes:
            for phon in range(0,len(word)-1):
                if word[phon] not in countDict:
                    countDict[word[phon]] = {word[phon+1]: 1}
                elif word[phon+1] in countDict[word[phon]]:
                    countDict[word[phon]][word[phon+1]] += 1
                else:
                    countDict[word[phon]][word[phon+1]] = 1
        return countDict

    def __str__(self):
        """
        When a FrequencyTable item is printed, this function is called to print a contingency table.
        arguments: a dictionary of dictionaries (self.frequency)
        returns: Nothing
        """
        for key in sorted(self.frequency):
            print '%-5s' % key,
        print('')
        for key in sorted(self.frequency):
            for subkey in sorted(self.frequency):
                if subkey in self.frequency[key]:
                    print '%-5s' % self.frequency[key][subkey],
                else:
                    print '%-5s' % '',
            print '%-5s' % key
        print '\n'
        return ""


mtnhs = FrequencyTable('./SampleTexts/mountainhouses.txt')
print(mtnhs)