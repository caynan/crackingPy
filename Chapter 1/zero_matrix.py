def find_zero(matrix):
    rows_to_zero = set()
    columns_to_zero = set()

    for i, line in enumerate(matrix):
        if i in rows_to_zero:
            continue
        for j, val in enumerate(line):
            if j in columns_to_zero:
                continue
            if val == 0:
                rows_to_zero.add(i)
                columns_to_zero.add(j)

    return rows_to_zero, columns_to_zero


def zero_out_rows(matrix, rows):
    for i in rows:
        matrix[i] = [0] * len(matrix[i])

    return matrix


def zero_out_columns(matrix, columns):
    for row in matrix:
        for j in columns:
            row[j] = 0

    return matrix


def zero_matrix(matrix):
    rows, columns = find_zero(matrix)
    matrix = zero_out_rows(matrix, rows)
    matrix = zero_out_columns(matrix, columns)

    return matrix


if __name__ == '__main__':
    m = [[0, 1 , 3], [32, 4, 5]]
    m_zero = [[0, 0, 0], [0, 4, 5]]

    assert zero_matrix(m) == m_zero
