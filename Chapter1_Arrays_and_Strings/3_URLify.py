class Solution:
    def urlify(self, input_string, true_length):
        """
            Time Complexity: O(n), where n is the true length of the input string
            Space Complexity: O(1)
        """
        # space_count = 0
        # for index in range(0, true_length):
        #     if input_string[index] == " ":
        #         space_count += 1
        # new_index = true_length + space_count*2

        # The input_string is assumed to have sufficient space at the end to hold the additional characters
        new_index = len(input_string)

        for index in reversed(range(true_length)):
            if input_string[index] == " ":
                input_string[new_index - 3 : new_index] = "%20"
                new_index -= 3
            else:
                input_string[new_index - 1] = input_string[index]
                new_index -= 1

        return input_string


if __name__ == '__main__':
    S = Solution()
    # Using lists because Python strings are immutable, they cannot be changed in place
    tests = [(list("Mr John Smith    "), 13),
        (list("much ado about nothing      "), 22),
        (list("a b c d e 20?date=2019-20-20          "), 28)]
    expected = [list("Mr%20John%20Smith"),
        list("much%20ado%20about%20nothing"),
        list("a%20b%20c%20d%20e%2020?date=2019-20-20")]
    total = len(tests)
    print("Testing urlify......")

    passed = 0
    for index in range(0, total):
        output = S.urlify(tests[index][0], tests[index][1])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed, total))