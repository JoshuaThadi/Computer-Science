# Iterative-Depth-First Search (DFS) Implementation
def iterative_dfs(graph, start_node):
    visited = set()  # to keep track of visited nodes
    stack = [start_node] # Stack using list
    
    while stack:
        vertex = stack.pop()  # remove the last element from the stack
        if vertex not in visited:
            print(vertex, end=" ")  # process the node
            visited.add(vertex)  # mark the node as visited
            
            # add unvisited neighbors to the stack
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
                
    print()  # for a new line after traversal
    
# Define the graph using an adjacency list (dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call the DFS function
print("DFS Traversal Order: ")
iterative_dfs(graph, 'A')  # Starting DFS from node 'A'
