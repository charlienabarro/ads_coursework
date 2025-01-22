
import random


def all_orderings(k):
    """
    Generates all Boldon House orderings of size k using backtracking.
    """
    all_orders = []
    count=0
    mod_list = []
    def backtracking(current,j,i,mod_list,repeat_num):
        if len(current) == k:
            return current

        elif len(current) == 0:
            current.append(j)
            backtracking(current,j,i,mod_list,repeat_num)

        elif len(mod_list) == 0:
            mod_list.append((j - current[-1]) % k)
            backtracking(current, j, i, mod_list, repeat_num)

        elif (j - current[-1])%6 >= mod_list[-1]:
            mod_list.append((j - current[-1])%6)
            repeat_num = 0
            return current.append(j)
        elif j>12:
            repeat_num +=1
            for z in range(len(current)):
                try:
                    backtracking(current[:-z],current[-z]+1,i,mod_list,repeat_num)
                except:
                    ...

        else:
            backtracking(current,j+1,i,mod_list)



    for i in range(k):
        current = []
        j=0
        backtracking(current, j, i, mod_list,0)



def ordering(k):
    """
    Returns a Boldon House ordering of size k.
    """
    bolden = False
    while not bolden:
        # Generate a list of numbers from 0 to k-1
        order = [i for i in range(k)]

        # Shuffle the list manually by swapping elements
        random.shuffle(order)
        mod_list = []
        # Calculate the pairwise differences modulo k
        for i in range(1, k):
            value = (order[i] - order[i - 1]) % k
            mod_list.append(value)

        correct = True
        # Check if the differences are monotone increasing
        for i in range(1,len(mod_list)-1):
            if mod_list[i+1] < mod_list[i]:
                correct = False
        if correct:
            bolden = True

    return order


print(all_orderings(12))

# simple test for all_orderings(k) only
# you do not have to return the Boldon House orderings in exactly the same order as they appear in this test case
'''assert(set(tuple(o) for o in all_orderings(3)) ==
       set(tuple(o) for o in [[0, 2, 1], [0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]))'''