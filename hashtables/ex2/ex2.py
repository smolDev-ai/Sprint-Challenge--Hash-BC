#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Added tickets to hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # hint mentioned route[i-1], so for loop?
    for i in range(length):
        if route[i-1] is not None:
            # finds key that exists
            route[i] = hash_table_retrieve(hashtable, route[i-1])
        else:
            # Ex1 mentions that retrieve returns none if key does not exist.
            route[i] = hash_table_retrieve(hashtable, "NONE")
    # return full array
    return route[:-1]
