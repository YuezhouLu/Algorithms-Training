class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # Helper function 1
    def add_node(self, head, node): # head is also a node
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = node
        return head
    
    # Helper function 2
    def list_values(self, head):
        results = []
        curr = head
        while curr is not None:
            results.append(curr.val)
            curr = curr.next
        return results


    def remove_dups(self, head):
        """
            Time Complexity: O(N), where N is the number of elements in the linked list.
            Space Complexity: O(N)
        """
        # A quick sanity check
        if head is None:
            return
        
        curr = head

        #1 Use a List and "count":
        # store = []
        # store.append(curr.val)
        # while curr.next:
        #     if store.count(curr.next.val) == 1: # Or > 0, the count will always be either 0 or 1.
        #         curr.next = curr.next.next
        #     else:
        #         store.append(curr.next.val)
        #         curr = curr.next
        # return head

        #2 Use a Set and "in":
        seen = set([curr.val])
        while curr.next:
            if curr.next.val in seen:
                curr.next = curr.next.next
            else:
                seen.add(curr.next.val)
                curr = curr.next
        return head


    # The "Runner" technique, or the second pointer technique, without buffer.
    def remove_dups_2(self, head):
        """
            Time Complexity: O(N^2)
            Space Complexity: O(1)
        """
        if head is None:
            return
        
        curr = head
        while curr:
            runner = curr
            while runner.next:
                if runner.next.val == curr.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curr = curr.next
        return head



if __name__ == "__main__":
    S = Solution()
    tests = [[2, 1, 4, 6, 3, 4, 4, 4], [2, 3, 4, 5]]
    expected = [[1, 2, 4, 6, 3], [1, 2, 3, 4, 5]]
    total = len(tests)
    print("Testing remove_dups......")
    
    passed = 0
    for index in range(total): # 2 tests in total
        head = Node(1) # Place the "head = Node(1)" here to reset the head for each time of testing.
        for num in tests[index]:
            input_head = S.add_node(head, Node(num))
        output = S.list_values(S.remove_dups(input_head))
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT:{}; OUTPUT:{}; EXPECTED:{}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed, total))
    
    passed = 0
    for index in range(total):
        head = Node(1)
        for num in tests[index]:
            input_head = S.add_node(head, Node(num))
        output = S.list_values(S.remove_dups_2(input_head))
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT:{}; OUTPUT:{}; EXPECTED:{}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{}) for method 2!!!".format(passed, total))
    else:
        print("{} of {} tests passed for method 2".format(passed, total))