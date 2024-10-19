def get_matrix(n, m, value):
    matrix = []
    for row in range(1, n + 1):
        list_1 = []
        matrix.append(list_1)
        for column in range(1, 1 + m):
            list_1.append(value)
        if matrix == 0:
            matrix = []
            print(matrix)


    return matrix



result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)






