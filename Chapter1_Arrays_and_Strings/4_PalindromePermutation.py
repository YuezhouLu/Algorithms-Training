class Solution:
    def palindrome_permutation(self, input_string):
        """
            Time Complexity: O(n), where n is the length of the input string.
            Space Complexity: O(1)
        """
        # Use a List
        table = [0 for _ in range(ord('z') - ord('a') + 1)]
        odd_count = 0

        def char_to_index(letter):
            a = ord('a')
            z = ord('z')
            A = ord('A')
            Z = ord('Z')
            val = ord(letter)
            if a <= val <= z:
                return val - a
            elif A <= val <= Z:
                return val - A
            else:
                return -1

        for char in input_string:
            table_index = char_to_index(char)
            if table_index != -1:
                table[table_index] += 1
                if table[table_index] % 2:
                    odd_count += 1
                else:
                    odd_count -= 1

        return odd_count <= 1


    def palindrome_permutation_2(self, input_string):
        """
            Time Complexity: O(n), we scan the string once for spaces and again to
                add to dictionary. This could be done in one step if we desired.
            Space Complexity: O(1), the maximum size of the dictionary used would
                be 26 key:value pairs. If the input string was 10000 characters this
                size wouldn't matter.
        """
        # Use a Dictionary
        input_string = input_string.replace(" ", "")
        count_dict = dict() # Max size 26 in English (all letters will be transformed to be lower case)
        odd_limit = 1
        for letter in input_string:
            lower_letter = letter.lower()
            count_dict[lower_letter] = count_dict.setdefault(lower_letter, 0) + 1

        # Check all the counts in the dictionary
        odd_seen = 0
        for count in count_dict.values():
            if count % 2 == 1:
                odd_seen += 1
                if odd_seen > odd_limit:
                    return False
        return True



if __name__ == '__main__':
    S = Solution()
    tests = ['Tact Coa', 'jhsabckuj ahjsbckj', 'Able was I ere I saw Elba',
        'So patient a nurse to nurse a patient so', 'Random Words',
        'Not a Palindrome', 'no x in nixon', 'azAZ']
    expected = [True, True, True, False, False, False, True, True]
    total = len(tests)
    print("Testing palindrome_permutation......")

    passed = 0
    for index in range(0, len(tests)):
        output = S.palindrome_permutation(tests[index])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed ,total))

    passed = 0
    for index in range(0, total):
        output = S.palindrome_permutation_2(tests[index])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{}) for method 2!!!".format(passed, total))
    else:
        print("{} of {} tests passed for method 2".format(passed, total))