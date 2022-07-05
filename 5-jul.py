class Node:
 
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next
class LinkedList:
  def __init__(self):  
    self.head = None
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
def merge(a1, a2): 
    head_ptr = temp_ptr = Node()  
    while a1 or a2:
        if a1 and (not a2 or a1.data <= a2.data):
            temp_ptr.next = Node(a1.data)
            a1 = a1.next
        else:
            temp_ptr.next = Node(a2.data)
            a2 = a2.next
        temp_ptr = temp_ptr.next
    return head_ptr.next

LL1 = LinkedList()
LL1.insert(7)
LL1.insert(5)
LL1.insert(3)
LL1.insert(1)
LL1.insert(20)

LL2 = LinkedList()
LL2.insert(6)
LL2.insert(25)
LL2.insert(32)
LL2.insert(11)
LL2.insert(9)
LL3 = LinkedList()
LL3.head=merge(LL1.head, LL2.head)
LL3.printLL()