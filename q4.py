def all_orderings(k):
    """
    Generates all Boldon House orderings of size k using backtracking.
    """
    all_orders = []

    def backtrack(current, mod_list):
        if len(current) == k:
            is_monotone = True
            for i in range(1, len(mod_list)):
                if mod_list[i] < mod_list[i-1]:
                    is_monotone = False
                    break
            if is_monotone:
                all_orders.append(current[:])
            return

        for num in range(k):
            if num not in current:
                if len(current) > 0:
                    diff = (num - current[-1]) % k
                    new_mod_list = mod_list + [diff]
                else:
                    new_mod_list = mod_list

                if len(new_mod_list) < 2 or new_mod_list[-1] >= new_mod_list[-2]:
                    current.append(num)
                    backtrack(current, new_mod_list)
                    current.pop()

    backtrack([], [])
    return all_orders


def ordering(k):
    """
    Returns a Boldon House ordering of size k.
    """
    result = []
    def backtrack(current, mod_list):

        if len(current) == k:
            is_monotone = True
            for i in range(1, len(mod_list)):
                if mod_list[i] < mod_list[i - 1]:
                    is_monotone = False
                    break
            if is_monotone:
                result.append(current[:])
            return

        for num in range(k):
            if num not in current:
                if len(current) > 0:
                    diff = (num - current[-1]) % k
                    new_mod_list = mod_list + [diff]
                else:
                    new_mod_list = mod_list

                if len(new_mod_list) < 2 or new_mod_list[-1] >= new_mod_list[-2]:
                    current.append(num)
                    backtrack(current, new_mod_list)
                    if result:
                        return
                    current.pop()

    backtrack([], [])

    return result[0] if result else []

assert(set(tuple(o) for o in all_orderings(3)) ==
       set(tuple(o) for o in [[0, 2, 1], [0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]))
