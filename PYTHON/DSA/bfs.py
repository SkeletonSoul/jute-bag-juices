# BREADTH FIRST SEARCH
# implement with a queue
# need a visited queue to maintain visited nodes
from collections import deque

def bfs(tree, start):
    queue = deque([start])
    visited = []

    while queue:
        node = queue.popleft()
        print(node, end = " ")
        visited.append(node)

        for child in tree[node]:
            if child not in visited and child not in queue:
                queue.append(child)

    return visited
        

tree = {
    1 : [2,3,4,5],
    2 : [6,7],
    3 : [8],
    4 : [9],
    5 : [],
    6 : [],
    7 : [10],
    8 : [],
    9 : [],
    10 : [1]
}

result = bfs(tree, 1)
