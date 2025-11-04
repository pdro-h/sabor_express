from collections import deque

def bfs(locations, distance_matrix, start, goal):
    num_nodes = len(locations)
    queue = deque([(start, [start], 0.0)])
    visited = set([start])
    while queue:
        current, path, cost = queue.popleft()
        for neighbor in range(num_nodes):
            if neighbor == current or neighbor in visited:
                continue
            new_path = path + [neighbor]
            new_cost = cost + distance_matrix[current][neighbor]
            if neighbor == goal:
                return new_path, new_cost
            visited.add(neighbor)
            queue.append((neighbor, new_path, new_cost))
    return [], float('inf')
