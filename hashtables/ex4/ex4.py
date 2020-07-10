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

# cache = {}

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



    # for interger in a:
    #     if interger == 0:
    #         pass
    #     #if negative integer in cache add it
    #     if -interger in cache:
    #         cache[-interger] +=1
    
    # result = []

    # # each interger in the cache that contains a key-value pair
    # for e in cache.items():
    #    #if the 2nd element in the array equals 2
    #     if e[1] ==2:
    #        #if first element in the array is less than 0, meaning is negative
    #         if e[0] < 0:
    #              #add that to the result array     
    #             result.append(-e[0])
    #          #else if the first element is greater than zero. A positive integer then add it to the result array
    #         else:
    #             result.append(e[0])


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
