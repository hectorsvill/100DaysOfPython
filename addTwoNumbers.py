class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(number):
    numArr = []
    while number > 0: 
        numArr.insert(0, number % 10)
        number //=10
    return numArr

def createLinkList(arr):
    if not arr:
        return None    
    head = ListNode(arr[0])
    node = head
    for n in arr[1:]:
        node.next = ListNode(n)
        node = node.next
    return head

def printLinkList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def addTwoNumbers(l1, l2):
    num1 = [] 
    num2 = []
    while l1 or l2:
        if l1 != None:
            num1.append(l1.val)
            l1 = l1.next
        if l2 != None:
            num2.append(l2.val)
            l2 = l2.next
    num1 = int("".join(map(str, num1)))
    num2 = int("".join(map(str, num2)))
    sum = num1 + num2
    

    sumList = []
    while sum > 0: 
        sumList.append(sum % 10)
        sum //=10

    print(sumList)
    head = ListNode(sumList[0])
    node = head
    for n in sumList[1:]: 
        node.next = ListNode(n)
        node = node.next

    printLinkList(head)
    return head

if __name__ == "__main__":
    arr1 = createList(243)
    arr2 = createList(564)
    head1 = createLinkList(arr1)
    head2 = createLinkList(arr2)
    printLinkList(head1)
    printLinkList(head2)
    s = addTwoNumbers(head1, head2)

