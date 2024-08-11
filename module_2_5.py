def get_matrix(n, m, value):
    matrix = []
    for row in range(n):
        A_list_ = []
        for colurn in range(m):
            A_list_.append(value)
        matrix.append(A_list_)
        return matrix

result1 = get_matrix(2, 2, 10) # result1 - исходный код (n)
result2 = get_matrix(3, 5, 42)  # result2 - исходный код (m)
result3 = get_matrix(4, 2, 13)  # result3 - исходный код (value)
print(result1)
print(result2)
print(result3)






