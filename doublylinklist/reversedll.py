class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
class doubly():
    def __init__(self):
        self.head=None
    def append(self,val):
        new_n=Node(val)
        if not self.head:
            self.head=new_n
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_n
        new_n.prev=curr
    def traverse(self):
        if self.head==None:
            print("Empty List")
            return
        temp=self.head
        while temp:
            print(temp.val,end=" ")
            temp=temp.next
        print()
    def revbrute(self):
        temp=self.head
        stack = []
        while temp:
            stack.append(temp.val)
            temp=temp.next
        temp=self.head
        while temp:
            e=stack.pop()
            temp.val=e
            temp=temp.next
        return self.head
    def revopti(self):
        if not self.head.next or not self.head:
            return self.head
        curr=self.head
        prev=None
        while curr:
            front=curr.next
            curr.next=prev
            curr.prev=front
            prev=curr
            curr=front
        self.head=prev
        return self.head

dl=doubly()
n=int(input("Enter number of nodes = "))
for i in range(n):
    val=input("Enter node value = ")
    dl.append(val)
print("Original LL = ")
dl.traverse()
print("Reversed LL = ")
# dl.revbrute()
dl.traverse()
print("Optimally Reversed LL = ")
dl.revopti()
dl.traverse()