class Solution:
    def string_compression(self, input_string):
        """
            Time Complexity: O(n), where n is the length of the input string.
            Space Complexity: O(m), where m is the length of the compressed string.
        """
        if input_string == " " or len(input_string) <= 2:
            return input_string

        # Use a list (items will be joined later, like the Java's StringBuilder)
        # rather than starting with an empty string to avoid string cancatenation (cancat takes O(n^2) time)
        compressed_string = []
        count_consecutive = 0
        for index in range(len(input_string)):
            if index != 0 and input_string[index] != input_string[index - 1]:
                compressed_string.append(input_string[index - 1] + str(count_consecutive))
                count_consecutive = 0
            count_consecutive += 1

        # Add the last repeated character
        compressed_string.append(input_string[-1] + str(count_consecutive))

        return min(input_string, ''.join(compressed_string), key = len)



if __name__ == "__main__":
    S = Solution()
    tests = ["aabcccccaaa", "abcdef", "aaa", "aa", " "]
    expected = ["a2b1c5a3", "abcdef", "a3", "aa", " "]
    total = len(tests)
    print("Testing string_compression......")

    passed = 0
    for index in range(total):
        output = S.string_compression(tests[index])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT:{}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed, total))