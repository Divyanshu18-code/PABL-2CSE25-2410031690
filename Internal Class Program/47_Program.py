#Given a matrix a of size n*m which represents a park,

def footpath_cost(a, queries):
    n, m = len(a), len(a[0])
    for r, c in queries:
        r -= 1; c -= 1
        sections = [
            [a[i][j] for i in range(0,r) for j in range(0,c)],
            [a[i][j] for i in range(0,r) for j in range(c+1,m)],
            [a[i][j] for i in range(r+1,n) for j in range(0,c)],
            [a[i][j] for i in range(r+1,n) for j in range(c+1,m)]
        ]
        cost = sum(min(sec) for sec in sections if sec)
        print(cost)

a = [[1,2,3],[4,5,6],[7,8,9]]
queries = [[2,2]]

footpath_cost(a, queries)