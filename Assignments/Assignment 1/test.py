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
    
def main():
    spiral = create_spiral(3)
    for row in spiral:
        print(row)
    
if __name__ == "__main__":
    main()