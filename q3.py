class HashTable():
    """Implements a simple hash table of size k, with all
    empty entries denoted as '-' at initialisation.

    You must not modify this code.

    Set up your hashtable as follows, with some sensible integer value for k:
        h = HashTable(k)

    For a HashTable h:
        h.lookup(pos) returns the data in position pos.
        h.add(pos, data) adds data in position pos.
        h.check(table) checks that the current entries are equal to
            table, which is represented as a list. This is only used for
            testing that the hash table contains what we expect.
        h.print_table prints h.
    """

    def __init__(self, k):
        self.__table = ["-"] * k

    def lookup(self, pos):
        return self.__table[pos]

    def add(self, pos, data):
        self.__table[pos] = data

    def check(self, table_of_data):
        return self.__table == table_of_data

    def print_table(self):
        print(self.__table)


def hash_quadratic(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the
    hash table after these insertions.

    Use just one HashTable instance inside this function.

    Use quadratic probing (see question for details) to resolve
    collisions.
    """
    ht = HashTable(17)
    for element in d:
        pos = (3*element + 5) % 17
        if ht.lookup(pos) == '-':
            ht.add(pos,element)
        else:
            solved = False
            count =1
            while not solved:
                new_pos = (pos + count ** 2) % 17
                if ht.lookup(new_pos) == '-':
                    ht.add(new_pos, element)
                    solved= True
                count += 1
            if count == 17:
                raise Exception('Table is full')
    return ht



def hash_double(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the
    hash table after these insertions.

    Use just one HashTable instance inside this function.

    Use double hashing (see question for details) to resolve
    collisions.
    """
    ht = HashTable(17)
    for element in d:
        pos = (3 * element + 5) % 17
        if ht.lookup(pos) == '-':
            ht.add(pos, element)
        else:
            step = 13 - (element % 13)
            count = 0
            while True:
                pos = (pos + step) % 17
                if ht.lookup(pos) == '-':
                    ht.add(pos, element)
                    break
                count +=1
            if count == 17:
                raise Exception('Table is full')
    return ht



# simple tests
assert (hash_quadratic([1, 2, 3, 4]).check([4, '-', '-', '-', '-', '-', '-', '-', 1, '-', '-', 2, '-', '-', 3, '-', '-']))
assert (hash_quadratic([5]).check(['-', '-', '-', 5, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))
assert (hash_quadratic([22]).check(['-', '-', '-', 22, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))
assert (hash_quadratic([5, 22, 39]).check(['-', '-', '-', 5, 22, '-', '-', 39, '-', '-', '-', '-', '-', '-', '-', '-', '-']))


assert (hash_double([1, 2, 3, 4]).check([4, '-', '-', '-', '-', '-', '-', '-', 1, '-', '-', 2, '-', '-', 3, '-', '-']))
assert (hash_double([5]).check(['-', '-', '-', 5, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))
assert (hash_double([22]).check(['-', '-', '-', 22, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))
assert (hash_double([5, 22, 39]).check(['-', '-', '-', 5, '-', '-', '-', 22, '-', '-', '-', '-', '-', '-', '-', '-', 39]))

# Test: Handling of full table (17 elements)
keys = [i for i in range(1, 18)]
assert hash_quadratic(keys).check([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
assert hash_double(keys).check([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
