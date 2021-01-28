# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0) # ListNode初始化地址
        head = l3 # head用来return的，因为循环内需要迭代到下一位
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        while l1 or l2 or carry:
            l3_sum, carry = carry, 0
            if l1 is not None:
                l3_sum += l1.val
                l1 = l1.next
            if l2 is not None:
                l3_sum += l2.val
                l2 = l2.next
            if l3_sum > 9:
                carry = 1
                l3_sum -= 10
            l3.next = ListNode(l3_sum) # 同时存好val和next
            l3 = l3.next
        return head.next