class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class SLinkList():
    def __init__(self):
        self.head=None
    def append(self,val):
        newn=Node(val)
        if self.head is None:
            self.head=newn
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newn
    def traverse(self):
        if self.head==None:
            print("List is empty")
        else:
            curr=self.head
            while curr:
                print(curr.val,end=" ")
                curr=curr.next
            print()
    def reversebruteforce(self):
        temp=self.head
        stack=[]
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        temp=self.head
        while temp is not None:
            e=stack.pop()
            temp.val=e
            temp=temp.next
        return temp
    def reverseoptim(self):
        temp=self.head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        self.head=prev
sll=SLinkList()
n=int(input("Enter number of nodes to be created: "))
for i in range(n):
    val=input("Enter value of node: ")
    sll.append(val)
print("Original List:-")
sll.traverse()
sll.reversebruteforce()
print("Reversed List:-")
sll.traverse()
sll.reverseoptim()
print("Reverse to reverse:- ")
sll.traverse()