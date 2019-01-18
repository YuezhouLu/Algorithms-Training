class Solution:
    def string_rotation(self, string1, string2):
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        def is_substring(string, sub):
            return string.find(sub) != -1
        
        length = len(string1)
        # Check that string1 and string2 are equal length and not empty.
        if length == len(string2) != 0:
            # Concatenate string1 and string1 within new buffer.
            string11 = string1 + string1
            return is_substring(string11, string2)
        return False



if __name__ == "__main__":
    S = Solution()
    tests = [
        ('waterbottle', 'erbottlewat'),
        ('foo', 'bar'),
        ('foo', 'foofoo'),
        ('foo', 'oof')
    ]
    expected = [True, False, False, True]
    total = len(tests)
    print("Testing string_rotation......")

    passed = 0
    for index in range(total):
        output = S.string_rotation(tests[index][0], tests[index][1])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed, total))