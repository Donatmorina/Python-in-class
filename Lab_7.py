
#Oppgave 1

#a) Yes this is a directed graph because the arrows point to what each number relate to,
#   0 is directed to 1
#   1 is directed to 2
#   2 is directed to 0 and 3
#   3 is directed to 4
#   4 is directed to 1

class Graph:
    graph = dict()
        
    def add_edge(self, node, neighbour):
            
        if node not in self.graph:
            self.graph[node] = [neighbour]

        else:
            self.graph[node].append(neighbour)

    def print_graph(self):

        print(self.graph)