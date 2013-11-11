# Comments on HW4

Author: Oliver  
Date: 2013-11-07

#### Overall

This is excellent work. The one weakness is in Problem 4, which is highly inefficient. Otherwise, nicely done!

#### Correctness

Excellent. All the outputs are perfect.

#### Readability

Excellent.

#### Documentation

Excellent. Great job using the verbose flag!

#### Efficiency

See my specific comments on Problem 4. In a nutshell, there are a few ways to solve this problem. The most elegant one is to use `.sub()` to make all the substitutions at once. The one in the spirit of the assignment uses `.finditer()` to do one sub at a time. This solution uses `string.split()`, which avoids the need for a regular expression at all, but here it's inside a loop that uses the `.finditer()` method. So the loop over the split string runs many more times than it needs to.