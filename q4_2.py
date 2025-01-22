def all_orderings(k):
    """
    Generates all Boldon House orderings of size k using backtracking.
    """
    all_orders = []

    def backtracking(current, mod_list):
        # If the order is complete, check if differences are monotone increasing
        if len(current) == k:
            correct = True
            for i in range(1, len(mod_list)):
                if mod_list[i] < mod_list[i-1]:
                    correct = False
                    break
            if correct:
                all_orders.append(current[:])  # Add a valid ordering
            return

        # Try adding each number from 0 to k-1 that hasn't been used
        for num in range(k):
            if num not in current:
                # Calculate the pairwise difference modulo k
                if len(current) > 0:
                    diff = (num - current[-1]) % k
                    new_mod_list = mod_list + [diff]
                else:
                    new_mod_list = mod_list  # No difference for the first number

                # Check if the differences are monotone increasing
                if len(new_mod_list) < 2 or new_mod_list[-1] >= new_mod_list[-2]:
                    current.append(num)
                    backtracking(current, new_mod_list)
                    current.pop()  # Backtrack by removing the last element

    backtracking([], [])
    return all_orders

# Example usage:

def check_order(order):
    mod_list = []
    for i in range(1,len(order)):
        mod_list.append((order[i] - order[i-1]) % k)
    for i in range(1,len(mod_list)):
        if mod_list[i] < mod_list[i-1]:
            return False
    return True
# Example usage:
k = 12
orders = all_orderings(k)
for order in orders:
    print(order)
    print(check_order(order))


