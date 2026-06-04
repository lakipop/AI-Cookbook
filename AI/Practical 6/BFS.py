from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([start])
    parent = {start: None}  # Track path

    visited.add(start)

    while queue:
        node = queue.popleft()

        if node == goal:
            # Reconstruct path
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    return None  # If no path found

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs_shortest_path(graph, 'A', 'F'))