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

    def list_values(self, head):
        results = []
        curr = head
        while curr is not None:
            results.append(curr.val)
            curr = curr.next
        return results


    def delete_middle_node(self, node):
        """
            Time Complexity: O(1)
            Space Complexity: O(1)
        """
        if node == None or node.next == None:
            return False
        else:
            node.val = node.next.val
            node.next = node.next.next



if __name__ == "__main__":
    S = Solution()
    tests = [  
        [2, 3, 4, 5],
        [200, 300, 400, 500, 600]
    ]
    expected = [
        [1, 2, 3, 5],
        [1, 200, 300, 500, 600]
    ]
    total = len(tests)
    print("Testing delete_middle_node......")

    passed = 0
    for index in range(total):
        head = Node(1)
        for num in tests[index]:
            input_head = S.add_node(head, Node(num))

        middle_node = input_head
        for _ in range(3): # Delete the 4th node for all tests
            middle_node = middle_node.next
        S.delete_middle_node(middle_node)
        
        output = S.list_values(input_head)
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed, total))