class Solution:
    def removeNthFromEnd(self,head: Optional[ListNode],n: int) -> Optional[ListNode]:
        lenn = 0
        curr = head

        while curr:
            lenn += 1
            curr = curr.next

        target = lenn - n

        if target == 0:
            return head.next

        init = 0
        start = head

        while init != target:
            init += 1

            if init == target:
                prev = start

            start = start.next

        prev.next = start.next

        return head