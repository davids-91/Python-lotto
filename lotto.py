import random


def get_input():
    numbers = input()
    number_list_string = numbers.split(" ")
    number_list = []
    for i in number_list_string:
        number_list.append(int(i))
    return number_list


def check_number_count(number_list):
    if len(number_list) == 6:
        return True
    else:
        return False


def check_unique(number_list):
    is_unique = True
    for i in number_list:
        if number_list.count(i) > 1:
            is_unique = False
            break
    return is_unique


def check_range(number_list):
    is_in_range = True
    for i in number_list:
        if not(1 <= i <= 49):
            is_in_range = False
            break
    return is_in_range


def generate_random_numbers():
    random_numbers = []
    for i in range(6):
        random_number = random.randint(1, 49)
        random_numbers.append(random_number)
    return random_numbers


def compare_results_and_output(random_number_list, number_list):
    hits = []
    count_of_hits = 0
    for random_number in random_number_list:
        for user_number in number_list:
            if user_number == random_number:
                hits.append(user_number)
                count_of_hits += 1
    print("Number of hits: " + str(count_of_hits))
    print("Lucky numbers are: " + str(hits))

