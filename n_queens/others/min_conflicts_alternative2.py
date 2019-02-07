# Created by Caleb Elliott

import random
from datetime import datetime

class minConflict(object):
    # Constructor for the minConflict class. Contains an 8 int array to represent the board
    # And a suitable swap candidates array
    def __init__(self, number_of_rows):
        self.rows = []
        self.candidates = []
        self.number_of_rows = number_of_rows

    # Function to check the number of conflicts given a row and column of a certain piece.
    # Returns the number of conflicts
    def check_conflicts(self, row, col):

        conflict_counter = 0
        # Iterates through the index of the rows array and checks for pieces in queens possible placements
        for val in range(len(self.rows)):
            # Check to make sure it does not count against itself
            if val != col:
                next_queen_row = self.rows[val]
                if next_queen_row == row or abs(next_queen_row - row) == abs(val - col):
                    conflict_counter += 1

        return conflict_counter

    # Function to initialize the board with 8 queens in an ideal layout
    def initialize_board(self):
        #iterates through the columns to place the queen
        for col in range(self.number_of_rows):
            #This is used to determine the bast placement. maxed out at 8
            min_conflict = 8
            #Flush the candidates array
            self.candidates = []
            #finds the rows with the least number of conflicts and adds them to the candidates array
            self.rows.append(0)
            for row in range(len(self.rows)):

                num_of_conflicts = self.check_conflicts(self.rows[row], col)
                if num_of_conflicts == min_conflict:
                    self.candidates.append(row)
                elif num_of_conflicts < min_conflict:
                    self.candidates = []
                    self.candidates.append(row)
                    min_conflict = num_of_conflicts
            #selects a random row from the suitable candidates array
            self.rows[col] =  random.choice(self.candidates)

    # Function to move the queen to the most suitable placement
    def move_queen(self, queen_col):
        # Flush the candidate array
        self.candidates = []
        # This is used to determine the best placement for the queen
        min_conflict = 8
        # Finds the rows with the least number of conflicts and adds them to the candidates array
        for val in range(len(self.rows)):
            conflict_num = self.check_conflicts(val, queen_col)
            if conflict_num == min_conflict:
                self.candidates.append(val)
            else:
                if conflict_num < min_conflict:
                    self.candidates = []
                    min_conflict = conflict_num
                    self.candidates.append(val)
        #If there are candidates set the queen to teh next best place
        if self.candidates:
            self.rows[queen_col] = random.choice(self.candidates)

    #Function to solve the board. uses a while loop to repeat itself. returns the number of turns it took to solve
    def solve_board(self):
        number_of_moves = 0
        while True:
            num_of_conflicts = 0
            self.candidates = []

            # Checks for the boards total conflicts
            for val in range(len(self.rows)):
                num_of_conflicts += self.check_conflicts(self.rows[val], val)
            # If there are no conflicts on the board return the moves
            if num_of_conflicts == 0:
                return number_of_moves

            # Choose a random queen to move and increase the move counter
            random_queen = random.randint(0,len(self.rows)-1)
            self.move_queen(random_queen)
            self.print_board()
            number_of_moves += 1


    # uses a nested for loop to print the board. Uses the rows array to deteermine where the queens should gp
    def print_board(self):
        rowprint = ''
        for r in range(len(self.rows)):
            for c in range(len(self.rows)):
                if self.rows[c] == r:
                    rowprint += "Q "
                else:
                    rowprint += "X "
            rowprint += "\n"
        print (rowprint)



def main(number_of_rows):
    # Create a new instance of the minConflict class
    random.seed(datetime.now())

    eightQueen = minConflict(number_of_rows)



    # Assigns the queens to their initial positions on the board then prints it
    eightQueen.initialize_board()
    eightQueen.print_board()

    #solves the given board and then prints it and the number of moves it had to take
    num_of_moves = eightQueen.solve_board()
    eightQueen.print_board()
    print("It took", num_of_moves, "moves to solve this board")




if __name__ == "__main__":
    main(20)