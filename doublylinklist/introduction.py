class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
print(n1.val)
print(n1)
print(n1.prev)
print(n2.prev)
print(n2)
print(n2.val)
print(n2.next)
print(n3)
print(n3.prev)
print(n3.next)
print(n3.val)