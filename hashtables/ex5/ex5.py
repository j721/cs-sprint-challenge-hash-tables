# Your code here

"""
Example input:

paths = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]

queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]
Example return value:

[ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]
"""


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    #create empty hash table
    hash = {}

    #traverse through individual files in the files list
    for i in files:
        #separate the file paths by "/"
        array = i.split("/")  
        #checking file name in the individual file paths      
        for element in array:
            #if not found return empty array
            if element not in hash:
                hash[element] = []
            #else add it into the hash table
            hash[element].append(i)

    result = []

    #traverse individual files through queries
    for x in queries:
        #if file found in hash table then add it into the result array
        if x in hash:
            result.extend(hash[x]) #extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
