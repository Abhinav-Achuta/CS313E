"""
    File: dna.py
    Description: Assignment 0, not graded, test

    Student Name: Abhinav Achuta
    Student UT EID: aa85934

    Partner Name:
    Partner UT EID:

    Course Name: CS 313E
    Unique Number: 52590
    Date Created: 8/23/2023
    Date Last Modified: 8/23/2023

    python dna.py < dna.in
"""


def longest_subsequence(string_1, string_2):
    """ADD YOUR CODE HERE """

    #Check what the longer string is
    long_string = ""
    short_string = ""
    string_1_len = len(string_1)
    string_2_len = len(string_2)

    if string_1_len > string_2_len:
        long_string = string_1
        short_string = string_2
    else:
        long_string = string_2
        short_string = string_1



def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """

    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
