
N, M = map(int, input().split())
edges = []
tree = []
info = []
for x in range(M):
    u, v = map(int, input().split())
    edges.append([u, v])

def findChildren(n):
    children = []
    for x in range(M):
        if edges[x][1] == n:
            children.append(edges[x][0])
            childN = findChildren(edges[x][0])
            for child in childN:
                children.append(child)
    return children

def generateTree():
    global tree
    for x in range(N):
        tree.append([x+1])
    for x in range(N):
        tree[x].append(findChildren(x+1))
    return tree

generateTree()

count = 0
for x in range(N):
    if len(tree[x][1]) % 2 == 1:
        count += 1
print(count - 1)
