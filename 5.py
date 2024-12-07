input_mat = [[1, 2], [3, 4], [5, 6]]


def reshape(mat, r, c):
    l = []
    for i in mat:
        for j in i:
            l.append(j)
    final = []
    if r*c == len(final):
        for i in range(0, r):
            final.append([])
            for j in range(0, c):
                final[i].append(l[0])
                l.pop(0)
        return final
    else:
        return mat

    


r = 2
c = 3

print(f"The input matrix was {input_mat} reshaped to {r} rows and {c} colums is {reshape(input_mat, r, c)}")

"""
Output:
The input matrix was [[1, 2], [3, 4], [5, 6]] reshaped to 2 rows and 3 columns is [[1, 2, 3], [4, 5, 6]]
"""
