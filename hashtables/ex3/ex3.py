"""

Find the intersection between multiple lists of integers.

Do not use numpy or sets to solve this; Big Hint: (use dict or hashtables, please). 

We're given a list of lists that contain integers:


And we need to compute the intersection, that is, numbers that exist in all lists.

"""





def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache ={}
    # Your code here
    # result = []

    # for array in arrays:
    #      for i in array:
    #          if i in cache:
    #              cache[i] +=1
    #          else:
    #             cache[i] = 1
    

    # for key,value in cache.items():
    #     if value == len(arrays):
    #         result.append(key)

      

    for array in arrays:
        for i in array:
            if i in cache:
                cache[i] +=1
            else:
                cache[i] = 1
    result = [data[0] for data in cache.items() if data[1] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
