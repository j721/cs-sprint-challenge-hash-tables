"""
For an input list of integers, we wish to know which positive numbers have corresponding negative numbers in the list.

looking for negative numbers that match

Example input:

[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
Input can be in any order.

Example return value:

[ 1, 3, 4 ] - output of all positive numbers

Because 1, 3, and 4 are the positive numbers that have corresponding negative numbers in the list.

Return value can be in any order.

Solve this problem with a hash table.

"""

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    #create cache dict to serve as hash table
    cache = {}
    #result is returned in an array
    result = []

    for interger in a:
        #if no interger in the cache array have value set to 1
        cache[interger] = 1
        #if interger is not zero and the negative interger is in the cache
        if interger !=0 and -interger in cache:
            #add the absolute value of the interger into the result array
            result.append(abs(interger))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
