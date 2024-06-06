
#Assignment 4 Domor6924

#1

# Given the following graph and looking at the arrows, we can clearly see that the answer here i d).
# This is because all the other answers have tuples that point the wrong directions such as (v3,v2) on answer c)
# Correct answer is d) { (v0,v1), (v1,v2), (v2,v3), (v3,v4), (v4,v0), (v0,v5), (v5,v4), (v3,v5), (v5,v2) }


#2

# Considering the given graph and their weights, the shortest path is 1) A -> C -> D -> E, the weight here is 19 because 
# from A -> C, the weight is 13, then from C -> D the weight is 1 and we just add that to 14 that becomes 14.
# Now finally from D -> E the weight is 5 and if we add that to 14, it becomes 19 wich makes this the shortest path compared to the other.


#3

COLUMNS = "abcde"
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []

def solve(partial_sol):
    exam = examine(partial_sol)
    
    if exam == ACCEPT:
       all_solutions.append(partial_sol)
    
    elif exam != ABANDON:
        
        for p in extend(partial_sol):
            solve(p)
    return all_solutions

def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):

            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON
    
    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE

def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])

    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])

    return (row1 == row2 or
            column1 == column2 or
            abs(row1 - row2) == abs(column1 - column2))

def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1

    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)

    return results


    
def is_solution(candidate_solution):
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            if attacks(candidate_solution[i], candidate_solution[j]):
                return "Invalid!"
    return "Valid!"


candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']
result1 = is_solution(candidate_solution1)
result2 = is_solution(candidate_solution2)
print("Candidate Solution 1:", result1)
print("Candidate Solution 2:", result2)


#4


class Graph:
    def __init__(self):
        self.graph = {}
 
    def add_vertex(self, vertex):

        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):

        if from_vertex not in self.graph:
            self.graph[from_vertex] = []

        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)
        self.graph[from_vertex].append(to_vertex)

    def print_graph(self):
        
        for vertex, edges in self.graph.items():
            print(vertex + ": " + str(edges))

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for vertices in list(self.graph):
                if vertex in self.graph[vertices]:
                    self.graph[vertices].remove(vertex)

    #eller:
    #def remove_vertex(self, vertex):
    #    self.graph[vertex] = []

graph = Graph()
graph.add_edge('a', 'b')
graph.add_edge('a', 'c')
graph.add_edge('b', 'c')
graph.add_edge('b', 'd')
graph.add_edge('c', 'd')
graph.add_edge('d', 'e')
print("Before removal of vertex:")
graph.print_graph()
graph.remove_vertex('a')
print("After removal of vertex:")
graph.print_graph()