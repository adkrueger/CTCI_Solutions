# if an element in an MxN matrix is a 0, then set the rest of the row/column to be zeros as well

def zero_matrix(m):
    # this can be done in O(2(nm)) time by first going through the array and recording which columns/rows need to be 0'd out,
    # then going through the matrix again and setting those cells to 0
    new_m = []

    col_dct = {}
    zeros = []
    flag = 0

    for i in range(len(m[0])):
        zeros.append(0)

    for i in range(len(m)):
        new_m.append([])
        flag = 0
        for j in range(len(m[i])):
            if m[i][j] == 0:
                col_dct[j] = 1
                
                if not flag:
                    new_m.append(zeros)
                    flag = 1
    
    print(new_m)

zero_matrix([[1, 2, 3],
             [4, 5, 6],
             [7, 0, 9],
             [1, 2, 0]])