from graphs import disjoint_set


def krushkal_mst():
    n = int(input())
    m = int(input())
    edges = []
    for i in range(0, m):
        u_v_wt = input().split()
        edges.append((int(u_v_wt[2]), (int(u_v_wt[0]), int(u_v_wt[1]))))

    edges = sorted(edges)
    print(edges)
    disjoint_set.init(n)

    ans = []
    totalWt = 0
    for wt, edge in edges:
        u = edge[0]
        v = edge[1]
        if disjoint_set.find_parent(u) != disjoint_set.find_parent(v):
            disjoint_set.union(u, v)
            totalWt += wt
            ans.append(edge)

    print('Miinum weight {} and Edges are{}'.format(totalWt, ans))


krushkal_mst()