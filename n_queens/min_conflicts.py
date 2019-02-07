import random
import time

# min-conflicts heuristic
def min_conflicts(csp, max_iters):
    for k in range(max_iters):
        conflicts_list = check_conflicts(csp)
        if len(conflicts_list) == 0:
            print("Solution: \n")
            print_csp(csp)
            print("")
            print(k, "iteractions executed \n")
            return
        random_var = random.choice(conflicts_list)
        min_conflicts_value = choose_min_conflicts_value(csp, random_var)
        csp_assign(csp, random_var, min_conflicts_value)
    raise Exception("Try more iteractions.")

def main(dim, max_iters):
    start_time = time.process_time()
    matrix = create_empty_matrix(dim)
    set_random_queens(matrix)
    min_conflicts(matrix, max_iters)
    end_time = time.process_time()
    print("Time:", end_time - start_time, "seconds")

# create an empty matrix DIMxDIM
def create_empty_matrix(dim):
    matrix = []
    for col in range(dim):
        matrix.append([]);
        for row in range(dim):
            matrix[col].append("[ ]");
    return matrix

# set randomly a queen per column in the matrix
def set_random_queens(matrix):
    queens_row_positions = []
    for col in range(len(matrix)):
        randomRow = random.randint(0, len(matrix) - 1)
        matrix[randomRow][col] = "[Q]"
        queens_row_positions.append(randomRow)

# choose a random row with min-conflicts for target column
def choose_min_conflicts_value(matrix, col):
    min_conf_num = len(matrix)
    min_conflicts_rows = []
    for row in range(len(matrix)):
        if matrix[row][col] != "[Q]":
            current_conflicts = len(check_element_conflicts(matrix, row, col))
            if current_conflicts < min_conf_num:
                min_conflicts_rows = []
                min_conf_num = current_conflicts
            if current_conflicts <= min_conf_num:
                min_conflicts_rows.append(row)
    return random.choice(min_conflicts_rows)

# reassign queen in a target column
def csp_assign(matrix, col, min_conflicts_row):
    for row in range(len(matrix)):
        matrix[row][col] = "[ ]"
    matrix[min_conflicts_row][col] = "[Q]"

# check total number of conflicts for whole matrix
def check_conflicts(matrix):
    total_conflicts_list = [];
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "[Q]":
                total_conflicts_list.extend(check_element_conflicts(matrix, row, col))
    return total_conflicts_list

# check the number of conflicts for a target queen
def check_element_conflicts(matrix, targetQueenRow, targetQueenCol):
    conflicts_list = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "[Q]":
                if col == targetQueenCol:
                    continue
                # check horizontal conflicts
                if row == targetQueenRow:
                    conflicts_list.append(col)
                # check diagonal conflicts
                if abs(col - targetQueenCol) == abs(row - targetQueenRow):
                    conflicts_list.append(col)
    return conflicts_list

# print matrix
def print_csp(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if col < len(matrix) - 1:
                print(matrix[row][col], end="")
            else:
                print(matrix[row][col])

# run
main(20, 1000)

