from math import floor,sqrt
from random import randint, shuffle
from copy import deepcopy


class Table:
    def __init__(self,size):
        self.table = []
        self.square_size = size
        self.max_number_in_square = pow(size,2)

        for i in range(0,self.max_number_in_square):
            self.table.append([0] * self.max_number_in_square)
    
    def show_table(self):
        for row in self.table:
            for col in row:
                if col:
                    print(col,end=" ")
                else:
                    print(' ',end=" ")
            print("")

    def load_grid(self,table):
        if len(table) == self.max_number_in_square:
            if str(table):
                self.table = table
        else:
            print("invalid size")

    def set_value(self,value,row,col):
        # check row & col
        for i in range(self.max_number_in_square):
            if self.table[row][i] == value or self.table[i][col] == value:
                return
        
        # Check Square
        cells_per_square = int(sqrt(self.max_number_in_square))
        first_cell_row_index = int(floor(row / cells_per_square) * cells_per_square)
        first_cell_col_index = int(floor(col / cells_per_square) * cells_per_square)

        for i in range(first_cell_row_index,first_cell_row_index+(cells_per_square-1)):
            for j in range(first_cell_col_index,first_cell_col_index+(cells_per_square-1)):
                if self.table[i][j] == value:
                    return
        
        # Passed all checks - set value
        self.table[row][col] = value

    def new_game(self,mode):
        # get list of all possible numbers
        all_numbers = list(range(1,self.max_number_in_square+1))

        # Optimization - Set 1 square 
        first_squre = all_numbers.copy()
        shuffle(first_squre)

        for row in range(self.square_size):
            for col in range(self.square_size):
                index_1d = (row*self.square_size)+col
                self.table[row][col] = first_squre[(row*self.square_size)+col]
        
        # Recurse and fill whole table
        self.table = self.generate_table(self.table,0,0,0,all_numbers)
        
        # Decide how many cells to clear
        if mode == 'easy':
            remove_goal = 43
        elif mode == 'medium':
            remove_goal = 51
        else: # Hard
            remove_goal = 56
            
        self.table = self.remove_cells(self.table,remove_goal)
        self.show_table()

    def generate_table(self,table,row,col,population_count,all_numbers):
        # End condition: table was fully populated
        if population_count == pow(self.max_number_in_square,2):
            return table
        
        # Increment cell position
        if col + 1 == self.max_number_in_square:
            next_col = 0
            next_row = row + 1
        else:
            next_col = col + 1
            next_row = row

        # If cell already has value - move to next cell
        # Else iterate all_numbers and try to populate
        if self.table[row][col]:
            return self.generate_table(deepcopy(table),next_row,next_col,population_count+1,all_numbers)
        else:
            shuffle(all_numbers)
            for number in all_numbers:
                if self.is_valid_placement(number,row,col,table):
                    table[row][col] = number
                    
                    new_table = self.generate_table(deepcopy(table),next_row,next_col,population_count+1,all_numbers)
                    if new_table != '':
                        return new_table
            return ''

    def remove_cells(self,table,remove_goal,removed_count=0):
        while remove_goal != removed_count:
            col = randint(0,self.max_number_in_square-1)
            row = randint(0,self.max_number_in_square-1)

            if table[row][col]:
                table[row][col] = None
                removed_count += 1
        return table
    
    def is_valid_placement(self,number,row,col,table=None):
        if not table:
            table = self.table

        # check row & col
        for i in range(self.max_number_in_square):
            if table[row][i] == number or table[i][col] == number:
                return False
        
        # Check Square
        first_cell_row_index = int(floor(row / self.square_size) * self.square_size)
        first_cell_col_index = int(floor(col / self.square_size) * self.square_size)

        for i in range(first_cell_row_index,first_cell_row_index+(self.square_size)):
            for j in range(first_cell_col_index,first_cell_col_index+(self.square_size)):
                if table[i][j] == number:
                    return False

        return True