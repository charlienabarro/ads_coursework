def max_consecutive_H(history, index=0, count=0, max_count=0):
    if index == len(history):
        return max_count

    if history[index] == 'H':
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

    return max_consecutive_H(history, index + 1, count, max_count)


def compute_winner(history_A, history_B):

    a_score = max_consecutive_H(history_A)
    b_score = max_consecutive_H(history_B)

    if a_score > b_score:
        return 'A'
    elif a_score < b_score:
        return 'B'
    else:
        return 'D'

def decode(compressed_string):
    letter_list = []
    values_list = []
    final_string = ''
    for i,letter in enumerate(compressed_string):
        if i%2 == 0:
            letter_list.append(letter)
        else:
            values_list.append(letter)

    for i,letter in enumerate(letter_list):
        final_string += letter*int(values_list[i])

    return final_string

def encode(string):
    result = ''
    count = 0
    last_letter = ''
    for letter in string:
        if letter == last_letter:
            count += 1
        else:
            result += last_letter + str(count)
            last_letter = letter
            count = 1
    result += last_letter + str(count)
    return result[1:]


def get_max_win_compressed(history):
    highest_num = 0
    for i,element in enumerate(history):
        if element == 'H':
            if int(history[i+1]) > highest_num:
                highest_num = int(history[i+1])
    return highest_num
def compute_winner_compressed(compressed_history_A,compressed_history_B):
    A_highest_num = get_max_win_compressed(compressed_history_A)
    B_highest_num = get_max_win_compressed(compressed_history_B)
    if A_highest_num > B_highest_num:
        return 'A'
    elif B_highest_num > A_highest_num:
        return 'B'
    else:
        return 'D'


print(encode('THTHTT'))
print(compute_winner_compressed('H1T2H2','T1H1T1H3T2'))

