"""
  File: spiral.py
  Description:

  Student Name: Abhinav Achuta
  Student UT EID: aa85934

  Partner Name:
  Partner UT EID:

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 8/30/23
  Date Last Modified: 8/30/23

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n

def create_spiral(n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
    
 Input: spiral is a 2-D list and n is an integer
 Output: returns an integer that is the sum of the
         numbers adjacent to n in the spiral
         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
"""

import math


def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""

    spiral = [[0]*dim for value in range(dim)]
    row, col = int(dim/2), int(dim/2) #Finding the center column for starting point
    current_cell = 1 #Labeling the starting with the value 1
    fill_direction = 0 # 0 -> right; 1 -> down; 2 -> left; 3 -> up

    while current_cell <= dim*dim: #Until the entire spiral is done, keep doing
        spiral[row][col] = current_cell #Giving the current cell its value

        if fill_direction == 0:
            col += 1 #Moving to the column to the right
            if col >= dim or spiral[row+1][col] == 0: #If at edge to right or below cell is 0 -> move down next
                fill_direction += 1
        
        elif fill_direction == 1:
            row += 1 #Moving the row down
            if row >= dim or spiral[row][col-1] == 0: #If at edge to bottom or cell to left is 0 -> move left next
                fill_direction += 1
        
        elif fill_direction == 2:
            col -= 1 #Moving column to the left
            if col < 0 or spiral[row-1][col] == 0: #If at edge to the left or cell above is 0 -> move up next
                fill_direction += 1

        elif fill_direction == 3:
            row -= 1 #Moving row up
            if row < 0 or spiral[row][col+1] == 0: #If at edge to the top or cell to right is 0 -> move right next
                fill_direction = 0 #Resetting direction

        
        current_cell += 1 #updating the cell number

    return spiral

def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    
    # ADD YOUR CODE HERE  


    return # ADD YOUR CODE HERE  





def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
