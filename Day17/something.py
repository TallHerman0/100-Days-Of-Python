#Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        incorrect1 = []
        incorrect2 = []
        correct = ListNode()
        string1 = ""
        string2 = ""
        answer = 0
        while current:
            #print(current.val)   # 2, then 4, then 3
            incorrect1.append(current.val)
            current = current.next

        current = l2
        while current:
            #print(current.val)   # 2, then 4, then 3
            incorrect2.append(current.val)
            current = current.next
        
        for num in range(len(incorrect1)-1,-1, -1):
            string1 += str(incorrect1[num])
        
        for num in range(len(incorrect2)-1, -1, -1):
            string2 += str(incorrect2[num])
        
        answer = int(string1) + int(string2)

        ans = str(answer)
        for number in range(len(ans)-1, -1, -1):
            print(ans[number])


l1 = ListNode(4)
l1.next = ListNode(5)
l1.next.next = ListNode(6)

l2 = ListNode(7)
l2.next = ListNode(8)
l2.next.next = ListNode(9)

Sol = Solution()

Sol.addTwoNumbers(l1, l2)