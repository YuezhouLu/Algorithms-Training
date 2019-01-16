class Solution:
    def rotate_matrix(self, matrix):
        """
            Time Complexity: O(n^2), where n is the length of the matrix, any algorithm must touch all N^2 elements.
            Space Complexity: O(1), inplace matrix APPEND and SLICE.
        """
        n = len(matrix)
        # A simple sanity check first.
        if n == 0 or n != len(matrix[0]):
            print("Not a NxN matrix!")
            return False

        else:
            for i in range(n):
                for j in range(n):
                    matrix[j].append(matrix[-1 - i][j])

                matrix[-1 - i] = matrix[-1 - i][n:] # Trick part!!!
                # At the end of each i's for loop, matrix_last_row[:n] becomes useless, and can be cut.
            return matrix


    def rotate_matrix_2(self, matrix):
        """
            Time Complexity: O(n^2), where n is the length of the matrix.
            Space Complexity: O(1), inplace four-way edge swap (index by index).
        """
        n = len(matrix)
        if n == 0 or n != len(matrix[0]):
            print("Not a NxN matrix!")
            return False
        else:
            for layer in range(n // 2):
                first, last = layer, n - layer - 1 # Trick part!!!
                # Need -1 here, because for 4x4 matrix, only swap 12 or N*(N - 1) rather than 16 or N^2 elements,
                # therefore, each time swap 3 items rather than 4 items.

                for i in range(first, last):
                    # Save Top
                    top = matrix[layer][i]

                    # Left -> Top
                    matrix[layer][i] = matrix[-1 - i][layer]

                    # Bottom -> Left
                    matrix[-1 - i][layer] = matrix[-1 - layer][-1 - i]

                    # Right -> Bottom
                    matrix[-1 - layer][-1 - i] = matrix[i][-1 - layer]
                    
                    # Top -> Right
                    matrix[i][-1 - layer] = top
            return matrix



if __name__ == "__main__":
    S = Solution()
    tests = [
        [   
            # Test a 4x5 matrix here
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19]
        ],
        [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]
        ],
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    ]
    expected = [
        False,
        [
            [12, 8, 4, 0],
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3]
        ],
        [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]
    ]
    total = len(tests)
    print("Testing rotate_matrix......")

    passed = 0
    for index in range(total):
        output = S.rotate_matrix(tests[index])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed, total))

    # Need to reset the tests here,
    # because the first method inplacely modifies and returns the input matrix.
    tests = [
        [   
            # Test a 4x5 matrix here
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19]
        ],
        [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]
        ],
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    ]

    passed = 0
    for index in range(total):
        output = S.rotate_matrix_2(tests[index])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{}) for method 2!!!".format(passed, total))
    else:
        print("{} of {} tests passed for method 2".format(passed, total))