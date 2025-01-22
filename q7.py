import random
def SelectPivotPair(L):
    """Return a pair (P0,P1) of pivot elements

    Select 5 distinct random elements from L, sort them,
    and let P0 be the second smallest and P1 the
    second largest of those 5 elements.
    """
    copy_l = L.copy()
    numbers= []
    for z in range(5):
        i = random.randint(0,len(copy_l)-1)
        numbers.append(copy_l[i])
        copy_l.pop(i)

    numbers = sorted(numbers)
    P0=numbers[1]
    P1=numbers[-2]
    return P0,P1





def ThreePartition(L,P0,P1):
    """Return a triple (L0,L1,L2) of sublists of L

    L0 consists of all elements of L smaller or equal P0,
    L1 of all elements of L larger than P0 but smaller or
    equal P1, and L2 of all elements of L larger than P1
    """
    pre_P0=[]
    between_P0_and_P1 = []
    post_P2 = []

    for number in L:
        if number<=P0:
            pre_P0.append(number)
        elif P0<=number<=P1:
            between_P0_and_P1.append(number)
        else:
            post_P2.append(number)

    return (pre_P0,between_P0_and_P1,post_P2)




def ThreeWayQuickSort(L):
    """Return a sorted version of L

    Use SelectPivotPair, ThreePartition and recursive
    calls to sort L.
    """
    if len(L)<=10:
        return sorted(L)
    pivots = SelectPivotPair(L)
    partitioned_list = ThreePartition(L,pivots[0],pivots[1])
    sorted_L1 = ThreeWayQuickSort(partitioned_list[0])
    sorted_L2 = ThreeWayQuickSort(partitioned_list[1])
    sorted_L3 = ThreeWayQuickSort(partitioned_list[2])

    return sorted_L1+ sorted_L2+sorted_L3


print(ThreeWayQuickSort([1,2,3,4,5,6,7,8,9,10,11]))
# simple tests

assert SelectPivotPair([5,4,3,2,1]) == (2,4)

assert ThreePartition([3,2,1],1,2) == ([1],[2],[3])

assert ThreeWayQuickSort([12,11,10,9,8,7,1,2,3,4,5,6]) == [1,2,3,4,5,6,7,8,9,10,11,12]

