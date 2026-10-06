class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class sing():
    def __init__(self):
        self.head=None
    def append(self,val):
        new=Node(val)
        if self.head==None:
            self.head=new
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new
    def traverse(self):
        if self.head==None:
            print("List is empty")
            return
        curr=self.head
        while curr is not None:
            print(curr.val,end=" ")
            curr=curr.next
        print()
    def oddevenlist(self):
        if self.head is None:
            print("Empty List")
            return
        if self.head.next is None:
            return self.head
        values=[]
        temp=self.head
        while temp:
            values.append(temp.val)
            if temp.next:
                temp=temp.next.next
            else:
                break
        temp=self.head.next
        while temp:
            values.append(temp.val)
            if temp.next:
                temp=temp.next.next
            else:
                break
        temp=self.head
        index=0
        while temp is not None:
            temp.val=values[index]
            index+=1
            temp=temp.next
        return self.head
    def odd_eve_optimal(self):
        if self.head is None or self.head.next is None:
            return self.head
        odd=self.head
        even=self.head.next
        even_head=even
        while even is not None and even.next is not None:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=even_head
        return self.head
sl=sing()
n=int(input("Enter number of nodes:- "))
for i in range(n):
    va=input("Enter value of node = ")
    sl.append(va)
print("Original LL = ")
sl.traverse()
print("Brute force even odd = ")
sl.oddevenlist()
sl.traverse()
print("Optimized even odd = ")
sl.odd_eve_optimal()
sl.traverse()