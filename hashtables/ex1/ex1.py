#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Goal: Create a solution that is O(n)
    # two unnested for loops?
    # simple subtraction? Addition and then move?
    # Add them to the hashtable first


    # Subtraction implementation
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        # subtract the limit from the current weight to get the number it
        # needs
        difference = hash_table_retrieve(ht, limit - weights[i])

        if difference is not None:
            return (difference, i)


    # Addition implementation
    # for i in range(length):
    #     hash_table_insert(ht, weights[i], i)

    # for i, j in enumerate(weights):
    #     unit_1 = weights[i]
    #     unit_2 = weights[j]
    #     print(unit_1, unit_2)


    #     if unit_1 is not None and unit_2 is not None:
    #         if unit_1 + unit_2 == limit:
    #             if unit_1 > unit_2:
    #                 return (unit_1, unit_2)
    #             else:
    #                 return (unit_2, unit_1)

    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
