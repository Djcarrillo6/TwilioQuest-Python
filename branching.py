import sys


first_number = int(sys.argv[1])
second_number = int(sys.argv[2])


def add_numbers(first_number, second_number):
    resulting_sum = first_number + second_number

    if resulting_sum <= 0:
        print("You have chosen the Path of destitution.")
    elif resulting_sum >= 1 and resulting_sum <= 100:
        print("You have chosen the path of plenty.")
    elif resulting_sum > 100:
        print("You have chosen the path of excess.")

    else:
        print("Nan 7")


add_numbers(first_number, second_number)
