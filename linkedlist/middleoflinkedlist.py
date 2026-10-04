class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class singleLL:
    def __init__(self):
        self.head=None
    def append(self,val):
        neu=Node(val)
        if self.head==None:
            self.head=neu
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=neu
    def traverse(self):
        if self.head==None:
            print("List is empty")
        else:
            cur=self.head
            while cur:
                print(cur.val,end=" ")
                cur=cur.next
            print()
    def find_middle(self): #brute force method
        if self.head==None:
            print("List is empty")
            return
        curr=self.head
        n=0
        while curr is not None:
            n=n+1
            curr=curr.next
        curr=self.head
        for i in range(0,n//2):
            curr=curr.next
        return curr
    def tortoise(self):
        slow=self.head
        fast=self.head
        while fast!=None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
sll=singleLL()
n=int(input("Enter number of nodes to be created: "))
for i in range(n):
    val=input("Enter value of node: ")
    sll.append(val)
print("Middle node is =",sll.find_middle().val)
print("Middle node is =",sll.tortoise().val)