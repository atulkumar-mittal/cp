parent = [0] * 10
rank = [0] * 10


def find_parent(node):
    if node == parent[node]:
        return node
    else:
        parent[node] = find_parent(parent[node])
        return parent[node]


def union(u, v):
    u_p = find_parent(u)
    v_p = find_parent(v)

    if u_p == v_p:
        return

    if rank[u_p] < rank[v_p]:
        parent[u_p] = v_p
    elif rank[u_p] > rank[v_p]:
        parent[v_p] = u_p
    else:
        parent[v_p] = u_p
        rank[u_p] += 1


def init(n):
    for i in range(0, n):
        parent[i] = i
        rank[i] = 0


if __name__ == '__main__':
    init(10)
    union(1, 2)
    union(2, 3)
    union(4, 5)
    union(6, 7)
    union(7, 8)
    union(5, 8)
    union(1, 9)

    print(parent)
    print(rank)