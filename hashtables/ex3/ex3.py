"""

Find the intersection between multiple lists of integers.

Do not use numpy or sets to solve this; Big Hint: (use dict or hashtables, please). 

We're given a list of lists that contain integers:

[
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

From the above input, the return value will be:

[1, 2]

And we need to compute the intersection, that is, numbers that exist in all lists.

"""


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
   
   #create a cache dictionary
    cache ={}

    #loop through the individual array inside of the larger array
    for array in arrays:
        #check for element in the individual array
        for i in array:
            #if element is in the cache then increment +=1
            if i in cache:
                cache[i] +=1
            #else element not in cache set the value to be 1
            else:
                cache[i] = 1
                
    #for each value in the cache starting the traversal from the first index
    #if the value is equal to the length of the larger arrays 
    # then return the result in the form of an array
    result = [value[0] for value in cache.items() if value[1] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
