class Solution:
    def one_away(self, string1, string2):
        """
            Time Complexity: O(n), where n is the length of the shorter string.
            Space Complexity: O(1)
        """
        # Length Check
        if abs(len(string1) - len(string2)) > 1:
            return False
        
        # Get shorter and longer strings. (Use Python ternary operator)
        short_str = string1 if len(string1) < len(string2) else string2
        long_str = string2 if len(string1) < len(string2) else string1

        index1 = 0
        index2 = 0
        found_difference = False
        while index1 < len(short_str) and index2 < len(long_str):
            if short_str[index1] != long_str[index2]:
                # Ensure that this is the first difference found.
                if found_difference:
                    return False
                found_difference = True

                if len(short_str) == len(long_str):
                    index1 += 1 # Situation 1: Replacement, move both index 1 and 2.
                else:
                    pass # Situation 2: Insertion or Removal, only move index 2 not 1.
            else:
                index1 += 1 # Situation 3: No edit, move both index.

            index2 += 1 # Always move index 2 no matter under which situation
        return True


    def one_away_2(self, string1, string2):
        """
            Time Complexity: O(n), where n is the length of the shorter string.
            Space Complexity: O(1)
        """
        def one_edit_replace(string1, string2):
            found_replacement = False
            for letter1, letter2 in zip(string1, string2):
                if letter1 != letter2:
                    if found_replacement == True:
                        return False
                    found_replacement = True
            return True

        def one_edit_insert(string1, string2):
            index1 = 0
            index2 = 0
            while index1 < len(string1) and index2 < len(string2):
                if string1[index1] != string2[index2]:
                    if index1 != index2:
                        return False
                    index2 += 1
                else:
                    index1 += 1
                    index2 += 1
            return True

        if len(string1) == len(string2):
            return one_edit_replace(string1, string2)
        elif len(string1) + 1 == len(string2):
            return one_edit_insert(string1, string2)
        elif len(string1) - 1 == len(string2):
            return one_edit_insert(string2, string1)
        else:
            return False



if __name__ == '__main__':
    S = Solution()
    tests = [('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'), ('paleabc', 'pleabc'), ('pale', 'ble'), 
        ('a', 'b'), ('', 'd'), ('d', 'de'), ('pale', 'pale'), ('pale', 'ple'), ('ple', 'pale'),
        ('pale', 'bale'), ('pale', 'bake'), ('pale', 'pse'), ('ples', 'pales'), ('pale', 'pas'),
        ('pas', 'pale'), ('pale', 'pkle'), ('pkle', 'pable'), ('pal', 'palks'), ('palks', 'pal')]
    expected = [True, True, True, True, False, True, True, True, True, True, True, True,
        False, False, True, False, False, True, False, False, False]
    total = len(tests)
    print("Testing one_away......")

    passed = 0
    for index in range(0, len(tests)):
        output = S.one_away(tests[index][0], tests[index][1])
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
    for index in range(0, len(tests)):
        output = S.one_away_2(tests[index][0], tests[index][1])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{}) for method 2!!!".format(passed, total))
    else:
        print("{} of {} tests passed for method 2".format(passed ,total))