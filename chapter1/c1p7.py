# given an NxN matrix, rotate the image by 90 degrees (clockwise?). can you do this in place?
'''
1 2 3            7 4 1
4 5 6     ->     8 5 2
7 8 9            9 6 3
'''
def rotate_matrix(m):
    # brute force: create another matrix and just iterate through the cells of m, assigning them to their properly rotated position
    
    new_m = []

    for i in range(len(m)):
        new_m.append([])
        for j in range(len(m[i])):
            new_m[i].append(m[len(m[i])-j-1][i])
    
    for i in new_m:
        print(i)

rotate_matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])