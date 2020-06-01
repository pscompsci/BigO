# Big-O and Algorithm Time Complexity

This repository runs a set of algorithms to produce data for graphs 
that show the time complexity of the algorithms,

The algorithms used have been chosen because they show the specific
time complexity desired for a particular graph.

In some cases, the Python interpreter applies optimizations that
reduce many of the algorithms to near constant time past a certain
point and specific steps have been taken to try to suppress
this behavior.

### Example:

If you loop over a range of values to calculate the sum, and O(n)
type algorithm, the Python interpreter applies a different approach
despite the code provided. 

Once the range of values reaches a certain point, the time taken
to calculate the sum reaches a constant value.

It is possible (though not confirmed) that the interpreter
instead uses the (n(n+1))/2 algorithm to calculate the sum, or is
caching results and then reusing them in subsequent calculations.

To suppress that behaviour, a list of random numbers is instead used
in this repository. That approach produces the expected O(n) 
performance.

<sub><sup>In loving memory of Grace Stacey (18/06/2003 - 01/01/2020)</sup></sub>