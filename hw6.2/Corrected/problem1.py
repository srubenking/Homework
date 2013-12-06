from runTregex import Treebank

pattern = "VP < (S < (/NP*+/ < -NONE-)) << (VP < TO) < (/VB(?!N)/ . S)"
dir = "C:\\Users\\Sophie\\Documents\\GitHub\\ComputationalMethods\\data\\Corpora\\treebank_3\\parsed\\mrg\\wsj"

'''
To find a control predicate we need to look for embedded sentences with a null subject

Because of the similarity in structure, we can't eliminate raising predicates such as "she seems to" or "it appears to"
'''
#!!! Excellent.

t = Treebank(dir,pattern)
t.run()


