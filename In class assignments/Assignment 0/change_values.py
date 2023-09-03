"""
In-Class Activity 0 solution
Class: C S 313E: Elements of Software Engineering
Run: 
python change_values.py < input.txt
3 1 0 3
"""
import math
import sys

def power_of_two(num):
    """Function determining if input number is a power of 2"""
    if num <= 0:
        return False
    return math.log2(num).is_integer()

def change_values(my_a: int, my_b: int, my_c: int, my_d: int):
    """Changes the values depending on ... """
    original_list = [my_a, my_b, my_c, my_d]
    new_list = []

    #If second value is odd then
    if my_b%2 != 0:
        new_list.append(original_list[1])
        new_list.append(original_list[0])
    else:
        new_list.append(original_list[0])
        new_list.append(original_list[1])

    #If third value is a power of two
    if power_of_two(original_list[2]):
        new_list.append(original_list[3])
        new_list.append(original_list[2])
    else:
        new_list.append(original_list[2])
        new_list.append(original_list[3])

    #Step 3
    if new_list[0] + new_list[1] + new_list[2] == new_list[3]:
        new_list[3] = new_list[0]


    return new_list

# You can add any helper function if needed.

def main():
    """A main function to read input data.
    No need to change this function 
    But feel free to change this if needed. 
    """
    data = sys.stdin.read()


    data_list = data.split('\n')
    data_list.remove('')
    data_list = [int(i) for i in data_list]

    # There are 4 values inside this list
    data_list_mutated = change_values(*data_list)
    print(*data_list_mutated)

if __name__ == '__main__':
    main()
