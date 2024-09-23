
def shape(mat):
    if len(mat) == 0 or len(mat[0]) == 0:
        return 0, 0
    r = len(mat)
    c = len(mat[0])
    return r,c

def create_matrix(r,c,value=0):
    matrix = []
    for each_r in range(r):
        row = []
        for each_c in range(c):
            row.append(value)
        matrix.append(row)
    return matrix

print(shape([[0,1],[1,2],[3,4]]))
print(create_matrix(5,5))
