#!/usr/env python

import subprocess
import json
from nltk.tree import *
import nltk.tree

import pdb

class SearchTree(ParentedTree):
    def adjacent(self,elt):
        '''
        Build a subclass of the SearchTree class in runTregex.py that contains a method adjacent(self, elt), which
        checks whether adjacent to self is a treelet bearing the elt as node label (for non-terminals) or value
        (in the case of leaves).

        Ran out of time so we weren't able to finish this part of the assignment. At the moment the functionality is
        limited to finding an adjacent sibling or cousin (the parents are siblings).
        '''
        if ParentedTree.left_sibling(self) == elt or ParentedTree.right_sibling(self) == elt:
            print 'adjacent'
        elif ParentedTree.left_sibling(self.parent()) == elt.parent() or ParentedTree.right_sibling(self.parent()) == elt.parent():
            print 'adjacent'
        else:
            print 'not adjacent'

    def loadMatches(self, e):
        self.e = e
        self.handles = {}
        self.handlePositions = {}
        self.filename = e["filename"]
        self.treenumber = e["treeNumber"]
        matchNumber = e["matchTreeNumber"] - 1
        self.matchTree = self.getTreeDepthFirstNumber(matchNumber)
        for handle,structure in e["nodes"].items():
            try:
                loc = int(structure["treeNumber"]) -1
                # NOTE: this doesn't deal with leaf handles, because they are strings; probably should stick with the tree positions...
                self.handles[handle] = self.getTreeDepthFirstNumber(loc)
                self.handlePositions[handle] = loc
            except:
                pass
    
    def getTreeDepthFirstNumber(self, num):
        return self[self.treepositions()[num]]
    
    def makeJSON(self, handles, position):
        out = {"name": self.node, "type": "nonterm" , "children": [], "position": position}

        # is this a handle, perhaps?
        for handle,treelet in handles.items():
            if treelet == self:
                out["handle"] = handle
                break
        
        
        for child in self:
            if isinstance(child, basestring): # is this a leaf?
                chOut,position = self.makeJSONleaf(child, handles, position+1)
            else:
                chOut,position = child.makeJSON(handles, position+1)
            out["children"].append(chOut)

        return (out, position)
    
    def makeJSONleaf(self, element, handles, position):
        out = {"name": element, "type": "term", "position": position}
    
        for handle,treelet in handles.items():
            if treelet == self:
                out["handle"] = handle
                break
        
        return (out, position)
        
class Treebank():

    javaJars = "../*;../stanford-tregex-2013-06-20/stanford-tregex.jar"
    javaPath = "/usr/bin/java"
    programLoc = "edu.ucsc.TregexWrapper.TregexWrapper"
    
    trees = []
    def __init__(self, dir, pattern, javaJars=None, javaPath=None):
        self.dir = dir
        self.pattern = pattern
        if javaJars:
            self.javaJars = javaJars

        if javaPath:
            self.javaPath = javaPath
        
    def run(self):
        self.trees = []
        print "Running tregex..."
        raw = subprocess.check_output(["java", "-cp", self.javaJars, self.programLoc, self.pattern, self.dir], stderr=subprocess.STDOUT)
        print "Processing output..."
        for ma in raw.split("\n"):
            try:
                m = json.loads(ma)
                tree = SearchTree(m["tree"])
            except:
                pass
            else:
                tree.loadMatches(m)
                self.trees.append(tree)
        print "Done!"

    def __getitem__(self, key):
        return self.trees[key]

    def __len__(self):
        return len(self.trees)

if __name__ == "__main__":
    dir = "C:/Users/Sophie/Documents/GitHub/ComputationalMethods/data/Corpora/treebank_3/parsed/mrg/wsj/24/"
    pattern = "(NP . NP)"
    
    t = Treebank(dir, pattern)
    t.run()
    test = t[0].matchTree
    test[0].adjacent(test)
    GM = t[0][0][0][0][0][0][0]
    s = t[0][0][0][0][0][1][0]
    print test.leaf_treeposition()