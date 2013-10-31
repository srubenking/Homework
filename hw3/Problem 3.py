#__author__ = scweiser and srubenking




def makeTable(pairs):
    """
    This takes the counting dictionary from before and prints a contingency table for it.
    arguments: a dictionary of dictionaries
    returns: Nothing
    """
    for key in sorted(pairs):
        print '%-5s' % key, #prints top row of phonemes, with cell space 5
    print ''
    for key in sorted(pairs):
        for subkey in sorted(pairs):
            if subkey in pairs[key]:
                print '%-5s' % pairs[key][subkey], #if the frequency of key:subkey is greater than 0, print it with cell space 5
            else:
                print '%-5s' % '', #otherwise, print an empty cell space 5
        print '%-5s' % key #print right column
    print '\n' #extra space after table
    return ""


testDict = {u'CH': {u'AH': 4}, u'D': {u'CH': 2}, u'AH': {u'K': 4, u'CH': 1}, u'K': {u'UH': 2}, u'M': {u'AH': 1}, u'IH': {u'F': 1}, u'HH': {u'AW': 1}, u'UH': {u'D': 6}, u'W': {u'UH': 4}}

makeTable(testDict)
