from runTregex import *
import re

dir = "C:\\Users\\Sophie\\Documents\\GitHub\\ComputationalMethods\\data\\Corpora\\treebank_3\\parsed\\mrg\\wsj\\24"
#using the entire wsj library took too long to process so we used the wsj\24 folder instead

allVerbs = "/VB.?/" #finds any verb
active = '/VB(?!N)/' #finds VB when not followed by 'N' which is the past participle marker
passiveBy = 'VBN > (VP <- (PP < (IN < by)))' #finds verb passive constructions with 'by'
passiveNoBy = 'VBN > (VP > (VP !< (/VB./ < /have|has|had|having|/)) !< PP)' #finds verb passive constructions without 'by'

allTrees = Treebank(dir,allVerbs)
allTrees.run() #searches for trees with any verb in them

countDict = {} #empty dictionary to store verb frequencies
for tree in allTrees:
    '''
    converts the subTree verb matches to strings then splits on word boundaries to extract the verb itself
    then makes entries for the dictionary 'countDict' in the format of 'verb : number of occurences' 
    '''
    subTree = str(tree.matchTree)
    subList = re.findall(r"[\w']+",subTree)
    verb = subList[1]
    if verb not in countDict:
        countDict[verb] = 1
    else:
        countDict[verb] += 1

activeTrees = Treebank(dir,active)
activeTrees.run() #searches for trees with active verbs in them

activeDict = {}
for tree in activeTrees:
    '''
    converts the subTree active verb matches to strings then splits on word boundaries to extract the verb itself
    then makes entries for the dictionary 'countDict' in the format of 'verb : number of occurences' 
    '''
    subTree = str(tree.matchTree)
    subList = re.findall(r"[\w']+",subTree)
    verb = subList[1]
    if verb not in activeDict:
        activeDict[verb] = 1
    else:
        activeDict[verb] += 1


passByTrees = Treebank(dir,passiveBy)
passByTrees.run() #searches for trees with passive verbs and a 'by' in them

passByDict = {}
for tree in passByTrees:
    '''
    converts the subTree passive 'by' verb matches to strings then splits on word boundaries to extract the verb itself
    then makes entries for the dictionary 'countDict' in the format of 'verb : number of occurences' 
    '''
    subTree = str(tree.matchTree)
    subList = re.findall(r"[\w']+",subTree)
    verb = subList[1]
    if verb not in passByDict:
        passByDict[verb] = 1
    else:
        passByDict[verb] += 1

passNoByTrees = Treebank(dir,passiveNoBy)
passNoByTrees.run() #searches for trees with passive verbs and no 'by' in them

passNoByDict = {}
for tree in passNoByTrees:
    '''
    converts the subTree passive 'no by' verb matches to strings then splits on word boundaries to extract the verb itself
    then makes entries for the dictionary 'countDict' in the format of 'verb : number of occurences' 
    '''
    subTree = str(tree.matchTree)
    subList = re.findall(r"[\w']+",subTree)
    verb = subList[1]
    if verb not in passNoByDict:
        passNoByDict[verb] = 1
    else:
        passNoByDict[verb] += 1

verbList = {'be':['is','was','were','am','are',"'s","'re","'m",'being','been'], #list of verb forms for the top 50 verbs in wsj\24
            'say':['said','says','saying'],
            'have':['has','had','having'],
            'do':['did','does','doing'],
            'sell':['sold','sells','selling'],
            'see':['sees','saw','seeing'],
            'buy':['buys','bought','buying'],
            'make':['makes','made','making'],
            'fall':['fell','fallen','falls','falling'],
            'get':['got','gets','gotten','getting'],
            'keep':['kept','keeps','keeping'],
            'begin':['begins','began','beginning'],
            'take':['takes','took','taken','taking'],
            'pay':['pays','paid','paying'],
            'put':['puts','putting'],
            'drop':['drops','dropped','dropping'],
            'think':['thinks','thought','thinking'],
            'include':['includes','included','including'],
            'give':['gives','gave','given','giving'],
            'agree':['agrees','agreed','agreeing'],
            'receive':['receives','received'],
            'expect':['expects','expected','expecting'],
            'want':['wants','wanted','wanting'],
            'work':['works','worked','working'],
            'accord':['accords','accorded','according'],
            'rise':['rises','rose','risen'],
            'set':['sets','setting'],
            'file':['files','filed','filing'],
            'call':['calls','called','calling'],
            'announce':['announces','announced','announcing'],
            'report':['reports','reported','reporting'],
            'help':['helps','helped','helping'],
            'close':['close','closed','closing'],
            'continue':['continues','continued','continuing'],
            'name':['names','named','naming'],
            'remain':['remains','remained','remaining'],
            'base':['bases','based','basing'],
            'become':['becomes','became','becoming'],
            'estimate':['estimates','estimated','estimating'],
            'leave':['leaves','left','leaving'],
            'hope':['hopes','hoped','hoping'],
            'raise':['raises','raised','raising'],
            'show':['shows','showed','shown','showing'],
            'go':['goes','went','going'],
            'seem':['seems','seemed','seeming'],
            'consider':['considers','considered','considering'],
            'return':['returns','returned','returning'],
            'use':['uses','used','using'],
            'spend':['spends','spent','spending'],
            'run':['runs','ran','running']}
totalVerbCountDict = {}

for verb in countDict: #searches through the dict of all verbs
    if verb in verbList: #checks if the verb is a base form in the verbList and adds the appropriate number of occurrences if it is
        if verb in totalVerbCountDict:
            totalVerbCountDict[verb] += countDict[verb]
        else:
            totalVerbCountDict[verb] = countDict[verb]
    else: #if the verb is not the base form, finds it within the verbList and adds the appropriate number of occurrences
        for base in verbList:
            if verb in verbList[base]:
                if base in totalVerbCountDict:
                    totalVerbCountDict[base] += countDict[verb]
                else:
                    totalVerbCountDict[base] = countDict[verb]

topActiveDict = {} #creates an empty dictionary to store active verb frequencies
for base in verbList:
    topActiveDict[base] = 0 #sets frequency for the verb to 0
    if base in activeDict:
        topActiveDict[base] += activeDict[base] #adds to the frequency count if the base form occurs as an active verb
    for form in verbList[base]:
        if form in activeDict:
            topActiveDict[base] += activeDict[form] #adds to the frequency count if any different form occurs as an active verb

topPassByDict = {} #creates an empty dictionary to store passive 'by' verb frequencies
for base in verbList:
    topPassByDict[base] = 0 #sets frequency for the verb to 0
    for form in verbList[base]: #skips the search for base forms because the passive is by definition the past participle
        if form in passByDict:
            topPassByDict[base] = passByDict[form] #if a passive 'by' form of the base verb is found, sets frequency equal to the frequency of the passive 'by' verb

topPassNoByDict = {} #creates an empty dictionary to store passive 'no by' verb frequencies
for base in verbList:
    topPassNoByDict[base] = 0 #sets frequency for the verb to 0
    for form in verbList[base]:
        if form in passNoByDict:
            topPassNoByDict[base] = passNoByDict[form] #if a passive 'no by' form of the base verb is found, sets frequency equal to the frequency of the passive 'no by' verb

sortedVerbs = sorted(totalVerbCountDict, key=totalVerbCountDict.get, reverse=True) #creates a list of top verbs sorted by number of total occurrences

print '%-10s' % 'Verb', '%-10s' % 'Active', '%-15s' % 'Passive No By', 'Passive By', #prints headers
print ''
for key in sortedVerbs: #prints a table with the base form of the verb and then the corresponding frequencies for active, passive 'no by', and passive 'by' forms
    print '%-10s' % key, '%-10s' % topActiveDict[key], '%-15s' % topPassNoByDict[key], topPassByDict[key]