class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class SinLL():
    def __init__(self):
        self.head=None
    def append(self,val):
        neu=Node(val)
        if self.head==None:
            self.head=neu
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=neu
    def traverse(self):
        if self.head==None:
            print("List is empty")
            return
        curr=self.head
        while curr:
            print(curr.val,end=" ")
            curr=curr.next
        print()
    def removfromendbrute(self,removal):
        if self.head==None:
            print("Empty list")
            return
        curr=self.head
        c=0
        while curr:
            c+=1
            curr=curr.next
        
        if removal==c:
            self.head=self.head.next
            return self.head
        pos_to_stop=c-removal
        curr=self.head
        count=1
        while count<pos_to_stop:
            curr=curr.next
            count+=1
        curr.next=curr.next.next
        return self.head
    def removend(self,pos):
        slow=self.head
        fast=self.head
        for _ in range(n):
            fast=fast.next
        if fast==None:
            return self.head.next
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return self.head
n=int(input("Enter number of nodes = "))
sl=SinLL()
for i in range(n):
    va=input("Enter value of node = ")
    sl.append(va)
rem=int(input("Enter position from end to remove = "))
print("Original Linklist = ")
sl.traverse()
print("Updated List = ")
sl.removfromendbrute(rem)
sl.traverse()
num=int(input("Enter number of nodes = "))
st=SinLL()

for i in range(num):
    va=input("Enter value of node = ")
    st.append(va)
re=int(input("Enter position from end to remove = "))
print("Original Linklist = ")
st.traverse()
print("Updated List = ")
st.removfromendbrute(re)
st.traverse()