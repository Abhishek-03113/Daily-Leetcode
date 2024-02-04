def linkedListToDecimal(head):
            decimal_value = 0
            while head: decimal_value, head = (decimal_value * 10) + head.data, head.next
            return decimal_value
        return Node(abs(linkedListToDecimal(list1) - linkedListToDecimal(list2)))
