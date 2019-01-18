class Solution:
    def zero_matrix(self, matrix):
        """
            Time Complexity: O(n)
            Space Complexity: O(1), where we use first row and column to keep track of all the rows and columns with zeros.
        """
        def nullify_row(matrix, row):
            for column in range(len(matrix[0])):
                matrix[row][column] = 0
        
        def nullify_column(matrix, column):
            for row in range(len(matrix)):
                matrix[row][column] = 0

        m = len(matrix)
        n = len(matrix[0])
        # Step 1
        first_row_has_zero = False
        first_column_has_zero = False
        # Check if first row has a zero.
        for column in range(n):
            if matrix[0][column] == 0:
                first_row_has_zero = True
                break
        # Check if first column has a zero.
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                first_column_has_zero = True
                break
        
        # Step 2
        # Check for zeros in the rest of the matrix.
        # Because we are checking the rest, thus range starts from 1!
        for row in range(1, m):
            for column in range(1, n):
                if matrix[row][column] == 0:
                    matrix[0][column] = 0
                    matrix[row][0] = 0
        
        # Step 3
        # Nullify rows based on values in first column.
        for row in range(m):
            if matrix[row][0] == 0:
                nullify_row(matrix, row)
        # Nullify columns based on values in first row.
        for column in range(n):
            if matrix[0][column] == 0:
                nullify_column(matrix, column)

        # Step 4
        # Nullify first row.
        if first_row_has_zero:
            nullify_row(matrix, 0)
        # Nullify first column.
        if first_column_has_zero:
            nullify_column(matrix, 0)

        return matrix


    def zero_matrix_2(self, matrix):
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        def nullify_row(matrix, row):
            for column in range(len(matrix[0])):
                matrix[row][column] = 0
        
        def nullify_column(matrix, column):
            for row in range(len(matrix)):
                matrix[row][column] = 0
        
        m = len(matrix)
        n = len(matrix[0])
        rows = []
        columns = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)
        
        for row_number in rows:
            nullify_row(matrix, row_number)
        for column_number in columns:
            nullify_column(matrix, column_number)
        
        return matrix



if __name__ == "__main__":
    S = Solution()
    tests = [
        [   
            [1, 2, 3, 4],
            [5, 0, 6, 7],
            [8, 9, 1, 2]
        ],
        [   
            [1, 0, 3, 4],
            [5, 6, 7, 8],
            [8, 0, 1, 2]
        ],
        [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    ]
    expected = [
        [   
            [1, 0, 3, 4],
            [0, 0, 0, 0],
            [8, 0, 1, 2]
        ],
        [
            [0, 0, 0, 0],
            [5, 0, 7, 8],
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ]
    ]
    total = len(tests)
    print("Testing zero_matrix......")

    passed = 0
    for index in range(total):
        output = S.zero_matrix(tests[index])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed, total))


    tests = [
        [   
            [1, 2, 3, 4],
            [5, 0, 6, 7],
            [8, 9, 1, 2]
        ],
        [   
            [1, 0, 3, 4],
            [5, 6, 7, 8],
            [8, 0, 1, 2]
        ],
        [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    ]

    passed = 0
    for index in range(total):
        output = S.zero_matrix_2(tests[index])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{}) for method 2!!!".format(passed, total))
    else:
        print("{} of {} tests passed for method 2".format(passed, total))