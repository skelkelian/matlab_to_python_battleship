matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

# for row in range(0, len(matrix)):
#     # print(row)
#     for col in range(0, len(matrix)-1):
#         print(type(matrix[row]))
#         print('row index: {} col index: {} value: {}'.format(row, col, matrix[row][col]))

matrix[1][1] = 100
# print(matrix)
# print(len(matrix))

def pretty_print_list(matrix):
    for row in range(0, len(matrix)):
        print(matrix[row])
        for col in range(0, len(matrix)-1):
            pass

pretty_print_list(matrix)
