# Breadth-First Search (BFS) Implementation
# BFS is a graph traversal algorithm that explores all nodes level by level starting from a given source node.
# It visits all neighbors of a node before moving to the next level neighbors.
# Often implemented using a queue.
# step-1: Define the graph using an adjacency list (dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# step-2: BFS function using a normal python list
def bfs(start_node):
    visited = []  # to keep track of visited nodes
    queue = [start_node]  # Queue using list
    print("BFS Traversal Order: ")
    
    while queue:
        node = queue.pop(0)  # remove the first element from the queue
        if node not in visited:
            print(node, end=" ")  # process the node
            visited.append(node)  # use append instead of add
            
            # add unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    print()  # for a new line after traversal

# step-3: Call the BFS function
bfs('A')  # Starting BFS from node 'A'