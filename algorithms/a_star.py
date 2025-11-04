# Menor custo/distancia
import heapq
import math

class GraphSearchAlgorithms:
    def __init__(self, locations_df, distance_matrix):
        self.locations = locations_df
        self.distance_matrix = distance_matrix
        self.num_nodes = len(locations_df)

    def heuristic(self, node_id, goal_id):
        x1, y1 = self.locations.loc[node_id, ['x', 'y']]
        x2, y2 = self.locations.loc[goal_id, ['x', 'y']]
        return math.hypot(x2 - x1, y2 - y1)

    def a_star(self, start, goal):
        open_set = [(0, start)]
        came_from = {}
        g_score = {i: float('inf') for i in range(self.num_nodes)}
        g_score[start] = 0
        f_score = {i: float('inf') for i in range(self.num_nodes)}
        f_score[start] = self.heuristic(start, goal)
        visited = set()
        while open_set:
            _, current = heapq.heappop(open_set)
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1], g_score[goal]
            visited.add(current)
            for neighbor in range(self.num_nodes):
                if neighbor == current:
                    continue
                tentative_g = g_score[current] + self.distance_matrix[current][neighbor]
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal)
                    if neighbor not in visited:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return [], float('inf')
