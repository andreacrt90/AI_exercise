import random
import time
import sys

# min-conflicts heuristic
def min_conflicts(csp, graph, colors, max_iters):
    for k in range(max_iters):
        conflicts_list = check_conflicts(csp, graph)
        if len(conflicts_list) == 0:
            print("\nSolution (state: color): \n")
            print_csp(graph)
            print("")
            print(k, "iteractions executed \n")
            return graph
        random_var = random.choice(conflicts_list)
        min_conflicts_value = choose_min_conflicts_value(csp, graph, colors, random_var)
        csp_assign(graph, random_var, min_conflicts_value)
    return {}

def main(csp, max_iters):
    start_time = time.process_time()
    colors_num = 3
    find_solution = False
    while find_solution == False:
        colors = generate_colors_list(colors_num)
        graph = create_empty_graph(csp)
        set_random_colors(graph, colors)
        graph = min_conflicts(csp, graph, colors, max_iters)
        if graph != {}:
            find_solution = True
        else:
            colors_num += 1
    end_time = time.process_time()
    print("It was used", colors_num, "colors. \n")
    print("Time:", end_time - start_time, "seconds")

# create empty graph
def create_empty_graph(csp):
    graph = {}
    for key in csp:
        graph[key] = ""
    return graph

# set randomly colors in the graphs
def set_random_colors(graph, colors):
    for key in graph:
        graph[key] = random.choice(colors)

# check total number of conflicts for whole graph
def check_conflicts(csp, graph):
    # csp contains states neighbors, graph contains states assigned colors
    total_conflicts_list = [];
    for key in csp:
        current_color = graph[key]
        # loop all neighbors and check if the color is the same
        for neighbor in csp[key]:
            if current_color == graph[neighbor]:
                total_conflicts_list.append(key)
    return total_conflicts_list

# choose a random state with min-conflicts neighbors
def choose_min_conflicts_value(csp, graph, colors, key):
    min_conf_num = sys.maxsize
    min_conflicts_color = []
    for color in colors:
        current_conflicts = check_conflicts_for_color(csp[key], graph, color)
        if current_conflicts < min_conf_num:
            min_conflicts_color = []
            min_conf_num = current_conflicts
        if current_conflicts <= min_conf_num:
            min_conflicts_color.append(color)
    return random.choice(min_conflicts_color)

# check the number of conflicts for a target state
def check_conflicts_for_color(neightbors, graph, color):
    conflicts = 0
    for neighbor in neightbors:
        if color == graph[neighbor]:
            conflicts += 1
    return conflicts

# reassign color to a target state
def csp_assign(graph, key, min_conflict_color):
    graph[key] = min_conflict_color

# print graph
def print_csp(graph):
    for key in graph:
        print(key, ": ", graph[key])

# generate random map with n states
def generate_random_map():
    map = {}
    states_list = []
    n = int(input("How many states? "))
    print("Generated random map (state: neighbors): \n")
    # create keys
    for i in range(n):
        key = "state" + str(i)
        states_list.append(key)
        map[key] = []
    # create values
    for j in map:
        # generate random links number
        links_num = random.randint(0, n - 1)
        for rand in range(links_num):
            state = random.choice(states_list)
            # add link if not already linked or repeated
            if state != j and j not in map[state] and state not in map[j]:
                map[j].append(state)
        print(j, ":", map[j])
    return map

# generate random colors list with n colors
def generate_colors_list(n):
    colors_list = []
    for i in range(n):
        color = "color" + str(i)
        colors_list.append(color)
    return colors_list


main(generate_random_map(), 1000)