class Solution:
    def check_inclusion(self, input_time, start_time, end_time):
        """
           this class method checks whether a given input_time is included between the given start_time and end_time,
           the range is 0 ~ 23, all the inputs are integer, and the ouput is expected to be a boolean, either True or False.
        """
        # Check the primary requirement whether all the inputs are between the 0 ~ 23 range, otherwise return False.
        if all(time >= 0 and time <= 23 for time in (input_time, start_time, end_time)):
            
            #1 The 1st case is that start_time is smaller than the end_time, e.g. 0 ~ 9,
            # When we want to check this case, it is really easy,
            # just return True if the input_time is between the two bounds. (start_time included, end_time excluded)
            if start_time < end_time:
                return input_time >= start_time and input_time < end_time
            
            #2 The 2nd case is that start_time is just equal to end_time, e.g. 6 ~ 6
            # and according to the question requirement, the input_time should be exactly equal to start_time or end_time,
            # otherwise, return False.
            elif start_time == end_time:
                return input_time == start_time # (if 6 ~ 6 means just 6, not any other time)
                # return True (if 6 ~ 6 means the entire time range, then this case 2 will always return True)
                # I am not sure which way this question means, but above are two answers for each way.

            #3 The 3rd case is that start_time is larger than end_time, if start_time > end_time, e.g. 15 ~ 3,
            # In the beginning (the very first if statement), we have maken sure that all 3 inputs are within 0 to 23,
            # therefore, if the input_time is larger than start_time, then the input_time must be in [start_time, 23(23 included)]
            # if the input_time is smaller than end_time, then the input_time must be in [0, end_time(end_time excluded)],
            # either of the two situations above should return True, otherwise, return False.
            else:
                return input_time >= start_time or input_time < end_time
 
        else:
            return False
# Solution Code ends here, below is the code for testing.
            

# Testing Section
if __name__ == "__main__":
    S = Solution()
    # We will carried out 6 tests here.
    tests = [[6, 0, 9], [12, 0, 9], [6, 6, 6], [5, 6, 6], [21, 15, 3], [2, 15, 3], [12, 15, 3], [100, 25, 37]]
    expected = [True, False, True, False, True, True, False, False]
    total = len(tests)
    passed = 0
    
    print("Testing check_inclusion......")

    for index in range(total):
        output = S.check_inclusion(tests[index][0], tests[index][1], tests[index][2])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT:{}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))

    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed, total))