from collections import deque

class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)


class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        visited = []
        stack = [self._root]
        result = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                result.append(current.value)

                for neighbor in reversed(current.outbound):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def bfs(self):
        visited = []
        queue = deque([self._root])
        result = []

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.append(current)
                result.append(current.value)

                for neighbor in reversed(current.outbound):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

g = Graph(a)

print(g.dfs())
print(g.bfs())