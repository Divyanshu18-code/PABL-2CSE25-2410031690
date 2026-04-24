#Given a integer matrix (or 2D array) a[][] of dimensions n * m. Also, given another 2-D array query[][] of dimensions q * 4.

def matrix_sum(a, queries):
    for q in queries:
        r1, c1, r2, c2 = q
        total = 0
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                total += a[i][j]
        print(total)


a = [[1,2,3],[4,5,6],[7,8,9]]
queries = [[0,0,2,2],[1,0,2,1]]
matrix_sum(a, queries)