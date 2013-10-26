# Comments on HW2

Author: Oliver  
Date: 2013-10-25

#### Overall

This is very good work overall. More specifically, it's generally excellent until Problem 7, which doesn't perform as intended.

#### Correctness

Problems 1-4 are clear and show a strong grasp of the material. Well done. Problem 5 has a small bug (repeated in Problem 7), where the loops need to start at 1 rather than 0. (See the specific comments to see why.) Problem 6 is again excellent. Given the degree of success on the earlier problems, however, Problem 7 is underwhelming. First, it doesn't look at all of the pronunciations of w1 and w2, which was an explicit requirement. Second, the alliteration function does not check whether the sounds being compared are consonants. Be careful to read the prompt fully before diving in. Finally, the bug from Problem 5 unfortunately prevents the rhyme function from working properly with vowel-initial words.

#### Readability

The code is generally readable. I'd steer clear of the minimalistic for-if-break combo as used here; just add an explicit variable setting before you break instead. This problem is compounded by misleading variable names like 'v1' for what is in fact a *substring* starting at the *last* vowel.

#### Documentation

The documentation is good. A little more on the tricky parts might have helped readability.

#### Efficiency

Excellent overall. No complains, beyond Problem 3, where redundancy could be avoided.