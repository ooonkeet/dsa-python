class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
class duble():
    def __init__(self):
        self.head=None
    def append(self,val):
        new=Node(val)
        if self.head is None:
            self.head=new
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new
        new.prev=curr
    def traverse(self):
        if not self.head:
            print("Empty list")
            return
        temp=self.head
        while temp:
            print(temp.val,end=" ")
            temp=temp.next
        print()
    def deleteocc(self,key):
        if self.head is None:
            return None
        temp=self.head
        while temp:
            if temp.val==key:
                if temp.prev is not None:
                    temp.prev.next=temp.next
                else:
                    self.head=temp.next
                if temp.next:
                    temp.next.prev=temp.prev
            temp=temp.next
        return self.head
dl=duble()
n=int(input("Enter number of nodes = "))
for i in range(n):
    val=input("Enter node value = ")
    dl.append(val)
print("Original LL")
dl.traverse()
key=input("Enter value to be deleted from list = ")
dl.deleteocc(key)
print("After deletion:- ")
dl.traverse()