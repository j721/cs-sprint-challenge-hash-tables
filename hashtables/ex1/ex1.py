"""

Merging Two Packages
Given a package with a weight limit limit and a list weights of item weights, 
implement a function get_indices_of_item_weights 
that finds two items whose sum of weights equals the weight limit limit. 

Your function will return a tuple of integers that has the following form:

(zero, one)
where each element represents the item weights of the two packages. 
The higher valued index should be placed in the zeroth index 
and the smaller index should be placed in the first index. If such a pair doesn’t exist for the given inputs, your function should return None.

Your solution should run in linear time.

Example:

Hints
How can we use a hash table in order to implement a solution with a better runtime?

Think about what we can store in the hash table in order to help us to solve this problem more efficiently.

What if we store each weight in the input list as keys? 
What would be a useful thing to store as the value for each key?

If we store each weight's list index as its value, 
we can then check to see if the hash table contains an entry for limit - weight. 
If it does, then we've found the two items whose weights sum up to the limit!

"""


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here



    return None
