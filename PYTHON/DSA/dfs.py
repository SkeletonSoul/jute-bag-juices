# DEPTH FIRST SEARCH
# implement with stack
def dfs(tree, start):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node)

        for child in reversed(tree[node]):
            if child not in visited and child not in stack:
                stack.append(child)

    return visited

tree = {
    1 : [2, 9, 10],
    2 : [3, 4],
    3 : [],
    4 : [5, 6, 7],
    5 : [8],
    6 : [],
    7 : [],
    8 : [],
    9 : [], 
    10 : []
}
result = dfs(tree, 1)
print(result)