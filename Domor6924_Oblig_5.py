
#1

# All trees given in the assignemt are full trees because the nodes have either 0 or 2 leaves (children)


#2

#The answer is (ii)

#  a   b    c    d    e    f    g    h 
#a 0   1    1    1    1    1    0    0

#b 0   0    1    0    1    0    0    0

#c 0   0    0    1    0    0    0    0

#d 0   0    0    0    1    0    0    0

#e 0   0    0    0    0    1    0    0

#f 0   0    1    0    0    0    1    1

#g 0   0    0    0    0    1    0    1

#h 0   0    0    0    0    1    1    0


#3
#class BinaryTree:

#    def __init__(self, value):
#        self.value = value
#        self.left_child = None
#        self.right_child = None

#    def insert_left(self, value):
#        if self.left_child is None:
#            self.left_child = BinaryTree(value)
#        else:
#            new_node = BinaryTree(value)
#            new_node.left_child = self.left_child
#            self.left_child = new_node
    
#    def insert_right(self, value):
#        if self.right_child is None:
#            self.right_child = BinaryTree(value)
#        else:
#            new_node = BinaryTree(value)
#            new_node.right_child = self.right_child
#            self.right_child = new_node

def make_tree(r):
    return [r, [], []]

def get_left_child(root):
    return root[1]
def get_right_child(root):
    return root[2]

def insert_left_child(root, new_branch):
    t = root.pop(1)
    if len(t)>1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], [], ])
    return root

def insert_right_child(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch,[], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


my_tree = make_tree("1")

insert_left_child(my_tree, "2")
insert_right_child(my_tree, "3")
insert_left_child(get_left_child(my_tree), "4")
insert_left_child(get_right_child(my_tree), "5")
insert_right_child(get_right_child(my_tree), "6")

print(my_tree)

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
        self.graph[from_vertex].append(to_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)

    def dfs(self, start):
        visited = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for x in self.graph.get(vertex, []):
                    if x not in visited:
                        stack.append(x)
        return visited

my_graph = Graph()

my_graph.add_vertex("a")
my_graph.add_vertex("b")
my_graph.add_vertex("c")
my_graph.add_vertex("d")
my_graph.add_vertex("e")

my_graph.add_edge("a", "d")
my_graph.add_edge("a", "c")
my_graph.add_edge("b", "a")
my_graph.add_edge("c", "b")
my_graph.add_edge("d", "e")
my_graph.add_edge("e", "a")

print(my_graph.graph)
print(my_graph.dfs("b"))

#5

class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        if self.value is not None:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None
        
    def is_empty(self):
        return self.value is None
        
    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        elif value < self.value:
            self.left_child.insert(value)
        elif value > self.value:
            self.right_child.insert(value)
    
    def compute_sum(self):
        if self.is_empty():
            return 0
        else:
            return self.value + self.left_child.compute_sum() + self.right_child.compute_sum()

    
    def compute_count(self):
        if self.is_empty():
            return 0
        else:
            return 1 + self.left_child.compute_count() + self.right_child.compute_count()


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)
my_tree.insert(12)
print('Sum:', my_tree.compute_sum())
print('Number of nodes:', my_tree.compute_count())
