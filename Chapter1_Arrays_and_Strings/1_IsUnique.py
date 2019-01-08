class Solution:
    def is_unique(self, input_string):
        """
            Time Complexity: O(min(c, n)), where n is the length of the input_string, and c is the size of the character set
            Space Complexity: O(c)
            Both time and space complexity can be argued to be O(1)
        """
        # Assuming character set is ASCII (128 characters)
        if len(input_string) > 128:
            return False
        
        char_set = [False for _ in range(128)]
        for char in input_string:
            unicode_point = ord(char)
            if char_set[unicode_point]:
                # Char already found in string
                return False
            char_set[unicode_point] = True
        return True

    def is_unique_2(self, input_string):
        """ 
            Sort then do linear check for neighboring characters in the string, without using additional data structures

            Time Complexity: O(nlog(n))
            Space Complexity: O(1)
        """
        input_string = sorted(input_string)
        if len(input_string) <= 1:
            return True
        for index in range(0, len(input_string) - 1): # No need to check the last character
            if input_string[index] == input_string[index + 1]:
                return False
        return True

    def is_unique_3(self, input_string):
        if len(input_string) != len(set(input_string)): # Use set()
            return False
        return True


if __name__ == "__main__":
    S = Solution()
    tests = ["abcd", "", "hb 627j=()", "testing", "23ds2", "hb 627jh=j ()"]
    expected = [True, True, True, False, False, False]
    total = len(tests)

    passed = 0
    for index in range(0, len(tests)):
        output = S.is_unique(tests[index])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    print("{} of {} tests passed".format(passed, total))

    passed = 0
    for index in range(0, len(tests)):
        output = S.is_unique_2(tests[index])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    print("{} of {} tests passed for alternative method 2".format(passed, total))

    passed = 0
    for index in range(0, len(tests)):
        output = S.is_unique_3(tests[index])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    print("{} of {} tests passed for alternative method 3".format(passed, total))