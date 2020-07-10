"""
where the source string represents the starting airport and the destination string represents the next airport 
along our trip. 
The ticket for your first flight has a destination with a source of NONE, 
and the ticket for your final flight has a source with a destination of NONE.


Hints:
The crux of this problem requires us to 'link' tickets together to reconstruct the entire trip.
 For example, if we have a ticket ('SJC', 'BOS') that has us flying from San Jose to Boston, 
    -from source to destination
 then there exists another ticket where Boston is the starting location, ('BOS', 'JFK').

We can hash each ticket such that the starting location is the key and the destination is the value. 
Then, when constructing the entire route, the ith location in the route can be found 
by checking the hash table for the i-1th location.

"""

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = []  

   #traverse through tickets lists
    for ticket in tickets:
        #ticket stored in cache and link together the source and destination
        cache[ticket.source] = ticket.destination
    #route set to default NONE
    route.append(cache['NONE'])
    #index element loop through length of the cache
    for i in range(length):
        #if we have a route found in the cache
        if route[i] in cache:
            #if at the first index of the route continue. source already defaulted to None
            if cache[route[i]] == route[0]:
                continue
            #if not at the first index, then update the route to be updated to have a source and destination defaulted to None
            route.append(cache[route[i]])



    return route

