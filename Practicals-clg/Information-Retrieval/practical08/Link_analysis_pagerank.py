# Aim: Link Analysis and PageRank 
# A) Implement the PageRank algorithm to rank web pages based on link 
# analysis. 
# B) Apply the PageRank algorithm to a small web graph and analyse the 
# results.

import numpy as np

def page_rank(graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
    # Number of nodes
    num_nodes = len(graph)

    # Initialize PageRank scores
    page_ranks = np.ones(num_nodes) / num_nodes

    for _ in range(max_iterations):
        prev_page_ranks = np.copy(page_ranks)

        for node in range(num_nodes):
            # Find nodes that link to this node
            incoming_links = [i for i, v in enumerate(graph) if node in v]

            if not incoming_links:
                continue

            page_ranks[node] = (
                (1 - damping_factor) / num_nodes
                + damping_factor *
                sum(prev_page_ranks[link] / len(graph[link]) for link in incoming_links)
            )

        # Convergence check
        if np.linalg.norm(page_ranks - prev_page_ranks, 2) < tolerance:
            break

    return page_ranks


# Example usage
if __name__ == "__main__":
    # Graph represented as adjacency list
    web_graph = [
        [1, 2],   # Node 0 links → 1, 2
        [0, 2],   # Node 1 links → 0, 2
        [0, 1],   # Node 2 links → 0, 1
        [1, 2],   # Node 3 links → 1, 2
    ]

    result = page_rank(web_graph)

    for i, pr in enumerate(result):
        print(f"Page {i}: {pr}")

print("\nPerformed by Joshua Thadi 48")
