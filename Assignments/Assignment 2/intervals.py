"""
    File: intervals.py
    Description: First we merged the tuples by comparing two values within the tuples.
    We then used the merged tuples and ordered the tuples based on the range of the tuples.

    Student Name: Abhinav Achuta
    Student UT EID: aa85934

    Partner Name: Seowon Jeong
    Partner UT EID: sj32632

    Course Name: CS 313E
    Unique Number: 52590
    Date Created: 9/4/23
    Date Last Modified: 9/4/23

    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
"""
import sys


def merge_tuples(tuples_list):
    """Merge the tuples"""

    merged_list = []

    tuples_list.sort()

    for interval in tuples_list:
        if not merged_list or interval[0] > merged_list[-1][1]:
            merged_list.append(interval)
        else:
            if interval[1] > merged_list[-1][1]:
                merged_list[-1] = (merged_list[-1][0], interval[1])

    return merged_list


def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """

    size_intervals = []
    sorted_list = tuples_list.copy()

    for i in tuples_list:
        size_intervals.append(i[1] - i[0])

    for i, _ in enumerate(tuples_list):
        count = 0
        for k, _ in enumerate(tuples_list):
            if size_intervals[i] > size_intervals[k]:
                count += 1
            if size_intervals[i] == size_intervals[k]:
                if tuples_list[i][0] > tuples_list[k][0]:
                    count += 1
        sorted_list[count] = tuples_list[i]

    return sorted_list



def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
