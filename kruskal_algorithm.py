class DisjointSet:
    def __init__(self, vertices):
        # Initialize each vertex as its own parent (subset) with a rank of 0
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        # Find the root of the set with path compression
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            # Attach the smaller rank tree under the root of the higher rank tree
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True  # A union occurred (no cycle)
        return False  # They are already in the same set (adding edge creates a cycle)


def kruskal(vertices, edges):
    """
    Computes the Minimum Spanning Tree (MST) using Kruskal's algorithm.
    :param vertices: List of all vertices (e.g., [0, 1, 2, 3])
    :param edges: List of tuples representing (weight, u, v)
    :return: List of edges included in the MST, and total MST weight
    """
    # 1. Sort all edges in non-decreasing order of their weight
    sorted_edges = sorted(edges, key=lambda edge: edge[0])
    
    dsu = DisjointSet(vertices)
    mst = []
    total_weight = 0

    # 2. Iterate through sorted edges
    for weight, u, v in sorted_edges:
        # If u and v do not belong to the same component, include the edge
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            
            # Optimization: Stop early if we have found V - 1 edges
            if len(mst) == len(vertices) - 1:
                break

    return mst, total_weight


# --- Example Usage ---
if __name__ == "__main__":
    # Define vertices
    nodes = [0, 1, 2, 3, 4]
    
    # Define edges as (weight, node1, node2)
    graph_edges = [
        (1, 0, 1),
        (7, 0, 2),
        (5, 1, 2),
        (4, 1, 3),
        (3, 1, 4),
        (6, 2, 4),
        (2, 3, 4)
    ]

    mst_edges, min_cost = kruskal(nodes, graph_edges)
    
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} -- {v} == Weight: {weight}")
    print(f"Total Minimum Cost: {min_cost}")
