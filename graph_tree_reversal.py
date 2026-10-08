from collections import deque

def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """Breadth-First Search using a Queue. Explores level-by-level."""
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """Depth-First Search using recursion."""
    visited = set()
    order = []

    def _dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)
    return order