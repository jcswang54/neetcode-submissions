# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()          # placeholder in front of the result
        tail = dummy                # last node of the merged list so far

        while list1 and list2:      # both lists still have nodes
            if list1.val <= list2.val:
                tail.next = list1   # attach the smaller node
                list1 = list1.next  # advance in that list
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next        # the attached node is now the tail

        tail.next = list1 if list1 else list2   # attach whatever remains
        return dummy.next           # skip the placeholder


        """head = list2 """
        """gives this linkedlist a name"""