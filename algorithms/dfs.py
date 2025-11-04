def dfs(locations, distance_matrix, start, goal):
    num_nodes = len(locations)
    stack = [(start, [start], 0.0)]
    visited = set([start])
    while stack:
        current, path, cost = stack.pop()
        for neighbor in range(num_nodes):
            if neighbor == current or neighbor in visited:
                continue
            new_path = path + [neighbor]
            new_cost = cost + distance_matrix[current][neighbor]
            if neighbor == goal:
                return new_path, new_cost
            visited.add(neighbor)
            stack.append((neighbor, new_path, new_cost))
    return [], float('inf')
