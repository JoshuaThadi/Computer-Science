# DFS implementation using adjacency list
# Depth first search uses stack [FILO] behavior 

def depthFirstSearch(graph, start, visited=None, traversal=None):
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []

    visited.add(start)
    traversal.append(start) # store node instead of printing immediately

    for neighbor in graph[start]:
        print(f"{start} -> {graph[start]}, neighbor => {neighbor}")
        if neighbor not in visited:
            depthFirstSearch(graph, neighbor, visited, traversal)
    return traversal

# example usage
if __name__ == "__main__":
    # graph represented as adjacency list (dictionary)
    graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }
    print("DFS Traversal starting from node A: ")
    traversal_result = depthFirstSearch(graph, 'A')
    print("\nFinal DFS Traversal result in Order: ", " -> ".join(traversal_result))



# visualization of the graph
'''
                A -- starting node (parent node)
               / \ -- branch
              B   C -- leaf node (child node)
             / \   \
            D   E   F
                |
                F -- ending node
'''

#Explanation
''' 
    A has two neighbors → B and C.
    B has two neighbors → D and E.
    E has one neighbor → F.
    C also points to F.
    D and F don’t have children.
'''
