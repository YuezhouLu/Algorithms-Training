class Solution:
    def check_permutation(self, string1, string2):
        """
            Time Complexity: O(n), where n is the length of the strings.
            Space Complexity: O(k), where k is the size of the counter.
        """
        if len(string1) != len(string2):
            return False
        counter = [0 for _ in range(128)]
        for char in string1:
            unicode_point = ord(char)
            counter[unicode_point] += 1
        for char in string2:
            unicode_point = ord(char)
            if counter[unicode_point] == 0:
                return False
            counter[unicode_point] -= 1
        return True


    def check_permutation_2(self, string1, string2):
        """
            Time Complexity: O(nlog(n))
            Space Complexity: O(1)
        """
        if len(string1) != len(string2):
            return False
        sorted_string1 = sorted(string1)
        sorted_string2 = sorted(string2)
        return sorted_string1 == sorted_string2



if __name__ == "__main__":
    S = Solution()
    tests = [["lll", "lll"], ["hello", "lleho"], ["Pacific", "Terrific"],
    ('abcd', 'bacd'), ('3563476', '7334566'), ('wef34f', 'wffe34'),
    ('abcd', 'd2cba'), ('2354', '1234'), ('dcw4f', 'dcw5f')]
    expected = [True, True, False, True, True, True, False, False, False]
    total = len(tests)
    print("Testing check_permutation......")
    
    passed = 0
    for index in range(0, len(tests)):
        output = S.check_permutation(tests[index][0], tests[index][1])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed, total))

    passed = 0
    for index in range(0, len(tests)):
        output = S.check_permutation_2(tests[index][0], tests[index][1])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{}) for method 2!!!".format(passed, total))
    else:
        print("{} of {} tests passed for method 2".format(passed, total))