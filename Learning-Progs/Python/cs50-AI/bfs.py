# Breath first search algorithm, BFS uses queue [FIFO] behaviour
from collections import deque

# BFS implementation using adjacency list
def breathFirstSearch(graph, start):
    visited = set()        # to keep track of visited nodes 
    queue = deque([start]) # queue for BFS 
    traversal = []         # store traversal order
    step = 1               # step counter

    while queue:
        node = queue.popleft() # take first element from queue 
        print(f"\nStep {step}:"); print(f"\nDequeue Node: {node}")

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            # add unvisited neighbors to queue 
            for neighbor in graph[node]:
                print(f"{start} : {graph[node]} => {neighbor}")
                if neighbor not in visited:
                    queue.append(neighbor)

        print(f"Queue: {list(queue)}"); 
        print(f"Visited: {visited}"); 
        print(f"Traversal: {traversal}")
        step = step + 1
    return traversal 

if __name__ == "__main__":
    #graph represented as adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("BFS traversal starting from node A: ")
    result = breathFirstSearch(graph, 'A')
    print("\nFinal BFS Traversal Order: "," -> ".join(result))

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
    Start at A, visit it → add B, C to queue.
    Visit B, add D, E.
    Visit C, add F.
    Visit D → no neighbors.
    Visit E, neighbor F (already in queue).
    Visit F → no neighbors.
    Last F skipped (already visited).
'''
