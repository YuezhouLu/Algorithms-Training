class Solution:
    def urlify(self, input_string, true_length):
        """
            Time Complexity: O(n), where n is the true length of the input string.
            Space Complexity: O(1)
        """
        # space_count = 0
        # for index in range(0, true_length):
        #     if input_string[index] == " ":
        #         space_count += 1
        # new_index = true_length + space_count*2

        # The input_string is assumed to have sufficient space at the end to hold the additional characters.
        new_index = len(input_string)

        for index in reversed(range(true_length)):
            if input_string[index] == " ":
                input_string[new_index - 3 : new_index] = "%20"
                new_index -= 3
            else:
                input_string[new_index - 1] = input_string[index]
                new_index -= 1

        return input_string


    def urlify_2(self, input_string, true_length):
        """
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        def char_check(c):
            if c == " ":
                return "%20"
            else:
                return c

        # The map() function executes a specified function for each item in a iterable,
        # the item is sent to the function as a parameter.
        return ''.join(map(char_check, list(input_string[:true_length])))


    def urlify_3(self, input_string, true_length):
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        def char_check(c):
            if c == " ":
                return "%20"
            else:
                return c

        result = ""
        for letter in input_string[:true_length]:
            result += char_check(letter)
        return result



if __name__ == '__main__':
    S = Solution()
    # Using lists because Python strings are immutable, they cannot be changed in place,
    # which means that we cannot change character in a string by directly calling 'string[index] = ...' in Python.
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

    # Need to reset the tests and expected here, because the first method return the input_string,
    # which modified the original tests, therefore the tests above cannot be used for later methods.
    tests = [("Mr John Smith    ", 13),
        ("much ado about nothing      ", 22),
        ("a b c d e 20?date=2019-20-20          ", 28)]
    expected = ["Mr%20John%20Smith",
        "much%20ado%20about%20nothing",
        "a%20b%20c%20d%20e%2020?date=2019-20-20"]
    total = len(tests)

    passed = 0
    for index in range(0, total):
        output = S.urlify_2(tests[index][0], tests[index][1])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{}) for method 2!!!".format(passed, total))
    else:
        print("{} of {} tests passed for method 2".format(passed, total))

    # No need to reset the tests and expected for method 3,
    # because map() in method 2 created a new list rather than modifying and returning the original input_string.
    passed = 0
    for index in range(0, total):
        output = S.urlify_3(tests[index][0], tests[index][1])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{}) for method 3!!!".format(passed, total))
    else:
        print("{} of {} tests passed for method 3".format(passed, total))