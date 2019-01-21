class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def add_node(self, head, node):
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = node
        return head

    # The following helper function is not needed in this question.
    # def list_values(self, head):
    #     results = []
    #     curr = head
    #     while curr is not None:
    #         results.append(curr.val)
    #         curr = curr.next
    #     return results


    # Recursive method
    def return_kth_to_last(self, head, k): # k should be an integer greater than or equal to 1.
        """
            Time Complexity: O(N), where N is the number of elements in the linked list.
            Space Complexity: O(1)
        """
        if head == None:
            return 0
        
        index = self.return_kth_to_last(head.next, k) + 1 # "self." is needed for recursive function calls.
        if index == k:
            print("%dth to last node is %s" % (k, head.val))
        
        return index


    # Iterative method
    def return_kth_to_last_2(self, head, k):
        """
            Time Complexity: O(N)
            Space Complexity: O(1)
        """
        runner = curr = head

        # Move runner k nodes into the list.
        for _ in range(k):
            if runner == None: # Out of bounds
                return None
            runner = runner.next

        # Move both runner and curr at the same pace.
        # When runner hits the end, curr will be at the right element.
        while runner:
            runner = runner.next
            curr = curr.next
        return curr.val



if __name__ == "__main__":
    S = Solution()
    tests = [
        [[2, 3, 4, 5], 1], 
        [[100, 200, 300, 400, 500, 600, 700, 800], 3]
    ]
    expected = [5, 600]
    total = len(tests)
    print("Testing return_kth_to_last......")

    # The first recursive method cannot be tested in the usual way (has to be checked manually),
    # because the answer is printed rather than returned. (Need a way to break out the recursive function...)
    for index in range(total):
        head = Node(1)
        for num in tests[index][0]:
            input_head = S.add_node(head, Node(num))
        output = S.return_kth_to_last(input_head, tests[index][1])

    passed = 0
    for index in range(total):
        head = Node(1)
        for num in tests[index][0]:
            input_head = S.add_node(head, Node(num))
        output = S.return_kth_to_last_2(input_head, tests[index][1])
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{}) for method 2!!!".format(passed, total))
    else:
        print("{} of {} tests passed for method 2".format(passed, total))