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


    def partition(self, head, pivot):
        """
            Time Complexity: O(N), where N is the number of elements in the linked list.
            Space Complexity: O(1)
        """
        curr = tail = head
        
        while curr:
            temp_saver = curr.next
            
            # # Unlike method 2, not necessary to isolate curr here.
            # curr.next = None

            if curr.val < pivot:
                curr.next = head
                # Very Very Tricky here!!!!!! (Pay attention!!!)
    
                # After the first time running through this step, curr = tail = head = [1, 5, 2, 4, 3]
                # all become curr = tail = head = [1] (actually is [1, 1, 1, 1......infinity], as the next of the node is the node itself.)
                # rather than [1, 1, 5, 2, 4, 3]. (the one I originally thought, but was wrong.)

                # "node.next = node" isolates and returns that node itself, becomes a ".next = self" infinitely looped single element.
                # If do not understand, refer to Example 3 of
                # https://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/linked%20lists.html
                
                head = curr

            else:
                tail.next = curr
                tail = curr

            curr = temp_saver
        
        # Unless the last element is larger than or equal to pivot, we need to do the following.
        tail.next = None


        # # Error check in case all nodes are less than pivot:
        # # Only needs the following codes if the curr was chosed to be isolated (not necessary for method 1 but for 2) at the beginning of each while loop.
        # # If all nodes are less than pivot, the tail will always be 1 (the first node of the input_head),
        # # and the next node of the tail is the tail itself which is 1 again (infinitely looped), therefore,
        # # we need the following if statement codes to cut off the infinite loop at the tail (the end of the output_head),
        # # in the case where all nodes are less than pivot.

        # # However, if there is at least one node greater than or equal to the pivot,
        # # then that node will just substitute the infinite loop and becomes the tail, which also helps us cut off the infinite loop at the same time.
        # if tail.next != None:
        #     tail.next = None
        
        return head


    def partition_2(self, head, pivot):
        """
            Time Complexity: O(N), where N is the number of elements in the linked list.
            Space Complexity: O(N)
        """
        #1 Prepare two linked lists: before and after.
        before_start = Node("null")
        before_end = Node("null")
        after_start = Node("null")
        after_end = Node("null")

        #2 Partition list and put each part into the before list or after list.
        curr = head
        while curr != None:
            #2.1
            # Save all the nodes after curr into a temp_saver.
            temp_saver = curr.next
            # Isolate the curr node by cutting the curr (setting the curr.next to be null)
            curr.next = None
            
            #2.2
            if curr.val < pivot:
                # Insert curr into end of before list.
                if before_start.val == "null":
                    before_end = before_start = curr
                else:
                    before_end.next = curr
                    before_end = curr # Reset the before_end to be the end of the before list.
            
            else:
                # Insert curr into end of after list.
                if after_start.val == "null":
                    after_end = after_start = curr
                else:
                    after_end.next = curr
                    after_end = curr
            
            #2.3
            # After processing a node (curr), reset the curr to be the temp_saver,
            # which is the new head of the input linked list.
            # In this way, we can loop through all the nodes in the input linked list.
            curr = temp_saver
        
        # # For testing
        # print self.list_values(before_start), self.list_values(after_start)
        
        #3 Merge before list and after list.
        if before_start == None:
            return after_start
        else:
            before_end.next = after_start
            return before_start



if __name__ == "__main__":
    S = Solution()
    tests = [
        [[5, 2, 4, 3], 3],
        [[3, 5, 8, 5, 10, 2, 1], 5]
    ]
    expected = [
        [2, 1, 5, 4, 3],
        [1, 2, 3, 1, 5, 8, 5, 10]
    ]
    total = len(tests)
    print("Testing partition......")

    passed = 0
    for index in range(total):
        head = Node(1)
        for num in tests[index][0]:
            input_head = S.add_node(head, Node(num))
        output = S.list_values(S.partition(input_head, tests[index][1]))
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{})!!!".format(passed, total))
    else:
        print("{} of {} tests passed".format(passed, total))
    

    tests = [  
        [[5, 2, 4, 3], 3],
        [[3, 5, 8, 5, 10, 2, 1], 5]
    ]
    expected = [
        [1, 2, 5, 4, 3],
        [1, 3, 2, 1, 5, 8, 5, 10]
    ]
    total = len(tests)

    passed = 0
    for index in range(total):
        head = Node(1)
        for num in tests[index][0]:
            input_head = S.add_node(head, Node(num))       
        output = S.list_values(S.partition_2(input_head, tests[index][1]))
        if output == expected[index]:
            passed += 1
        else:
            print("Test #{} Failed! INPUT: {}; OUTPUT: {}; EXPECTED: {}".format(
                index + 1, tests[index], output, expected[index]))
    if passed == total:
        print("All tests passed({}/{}) for method 2!!!".format(passed, total))
    else:
        print("{} of {} tests passed for method 2".format(passed, total))