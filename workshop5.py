import random


def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)

    print(random_number)
    while tries:  # while tries != 0 while tries is not 0, while tries is True
        guess = int(input("Guess a number between 0 and 10: "))
        if guess == random_number:
            print(f'your guess was {guess}')
            print(random_number)
            print("You have guessed correctly")
            break
        elif guess > random_number:
            print(f'your guess was {guess}')
            print("Guess lower!")
            tries -= 1
            print(bool(tries))
            print(f"You have {tries} left")
            continue
        elif guess < random_number:
            print(f'your guess was {guess}')
            print("Guess higher!")
            tries -= 1
            print(bool(tries))
            print(f"You have {tries} left")
            continue

    print("You have run out of tries")
    print(f'the correct number was {random_number}')


def guess_linear_search(tries, start, stop):
    random_number = random.randint(start, stop)
    number_range = range(start, stop + 1)
    the_list = list(number_range)
    print(the_list)
    for num in the_list:
        computer_guess = num
        print(f'The number for the program to guess is {random_number}')
        if num == random_number:
            print(f'The program has guess correctly and was {num}')
            break
        elif tries == 0:
            print(
                f'The program ran out of tries and was guessed incorrectly at {num}')
            break
        else:
            tries -= 1
            print(f"You have {tries} tries left")
            print(
                f'The program has failed to guess the number correctly and was {num}')
            continue


# guess_linear_search(5, 0, 10)

# guess_random_num_binary()

# def bubblesort(the_list):
#     high_idx = len(the_list) - 1

#     for i in range(high_idx):
#         list_changed = False
#         for j in range(high_idx):
#             item = the_list[j]
#             next = the_list[j+1]

#             if item > next:
#                 the_list[j] = next
#                 the_list[j+1] = item
#                 list_changed = True

#             print(the_list, i, j)
#         print(list_changed)
#         if list_changed == False:
#             break


def binary_search(tries, start, stop, the_list, target):
    number_range = range(start, stop + 1)
    the_list = list(number_range)
    lower_bound = 0
    upper_bound = len(the_list)-1
    print(f'The number the program is suppose to guess is {target}')
    while lower_bound <= upper_bound:
        # using floor division so we don't get a decimal split like 2.5 in a list of 5
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == target:
            print(f'The program guessed correctly at {pivot}')
            return pivot

        elif tries == 0:
            print("You've run out of tries")
            break
        elif pivot_value > target:
            upper_bound = pivot - 1
            tries -= 1
            print(f'{tries} tries left')
            print(f'The program guessed {pivot_value}')
        else:
            lower_bound = pivot + 1
            tries -= 1
            print(f'{tries} tries left')
            print(f'The program guessed {pivot_value}')
    return -1


start = 0
stop = 100
number_range = range(start, stop + 1)
the_list = list(number_range)


binary_search(5, 0, 100, the_list, 55)


# def binary_search(the_list, target):
#     lower_bound = 0
#     upper_bound = len(the_list) - 1

#     while lower_bound <= upper_bound:
#         pivot = (lower_bound + upper_bound) // 2 # using floor division so we don't get a decimal split like 2.5 in a list of 5
#         pivot_value = the_list[pivot]

#         if pivot_value == target:
#             return pivot
#         if pivot_value > target:
#             upper_bound = pivot - 1
#         else:
#             lower_bound = pivot + 1

#     return -1

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(binary_search(test_list, 10))
# print(binary_search(test_list, 4))
# print(binary_search(test_list, 33))
