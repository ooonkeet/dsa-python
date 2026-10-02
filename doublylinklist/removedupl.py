class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class Double():
    def __init__(self):
        self.head=None
    def append(self,val):
        neu=Node(val)
        if not self.head:
            self.head=neu
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=neu
        neu.prev=curr
    def traverse(self):
        if not self.head:
            print("Empty List")
            return
        curr=self.head
        while curr:
            print(curr.val,end=" ")
            curr=curr.next
        print()
    def deleterepocc(self):
        temp=self.head
        while temp and temp.next:
            if temp.val==temp.next.val:
                temp.next=temp.next.next
                if temp.next:
                    temp.next.prev=temp
            else:
                temp=temp.next
        return self.head
dll=Double()
n=int(input("Enter number of nodes = "))
for i in range(n):
    val=input("Enter node value = ")
    dll.append(val)
dll.traverse()
print("Deleted duplicates = ")
dll.deleterepocc()
dll.traverse()