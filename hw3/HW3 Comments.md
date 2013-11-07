# Comments on HW3

Author: Oliver  
Date: 2013-11-07

#### Overall

This is really excellent work. The solutions show a lot of care and were a pleasure to read through. Nicely done.

#### Correctness

Excellent overall. One point worth mentioning is that the solution to Problem 3, while elegant, misses a little data. The considers all pairs of phonemes that can be constructed from the keys of the frequency dictionary. This means, though, that if there's a phoneme that occurs only as the second member of a pair (or multiple pairs), it'll get passed over. With a big enough input, this might not be a problem, but given that certain sounds (like engma) are more likely to be found in the back half of a word than the front half, short inputs (like the woodchuck line) are pretty likely to miss something.

#### Readability

Excellent.

#### Documentation

Excellent. Just right.

#### Efficiency

Good. Pay attention to superfluous conditions in loops. Your code (from Problem 4, for example):

    def phonemeList(self):
        phonemeListOut = []
        for word in self.tokens:
            phonemeRep = None
            if word in dictionary:
                phonemeRep = dictionary[word][0]
            if phonemeRep != None:
                phonemeListOut.append(phonemeRep)
        return phonemeListOut

produces the same output as

    def phonemeList(self):
        phonemeListOut = []
        for word in self.tokens:
            if word in dictionary:
                phonemeRep = dictionary[word][0]
                phonemeListOut.append(phonemeRep)
        return phonemeListOut

But it involves the extra steps of setting a new variable and comparing it with None, even on iterations where those steps don't accomplish anything.