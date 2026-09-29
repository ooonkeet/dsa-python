class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
class doubleLL():
    def __init__(self):
        self.head=None
    def insert_at_head(self,val):
        new_n=Node(val)
        if not self.head:
            self.head=new_n
        else:
            new_n.next=self.head
            self.head.prev=new_n
            self.head=new_n
    def append(self,val):
        new_n=Node(val)
        if self.head is None:
            self.head=new_n
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_n
        new_n.prev=curr
    def insert_at(self,val,pos): 
        if pos==0:
            self.insert_at_head(val)
            return
        new_n=Node(val)
        curr=self.head
        c=0
        while curr and c<pos-1:
            curr=curr.next
            c+=1
        if curr is None:
            print("Positions out of bounds")
            return
        new_n.next=curr.next
        new_n.prev=curr
        if curr.next:
            curr.next.prev=new_n
        curr.next=new_n
    def traverse(self):
        if self.head==None:
            print("Empty list")
            return
        temp=self.head
        while temp:
            print(temp.val,end=" ")
            temp=temp.next
        print()
    def delete_head(self):
        if self.head==None:
            print("List is empty")
            return
        self.head=self.head.next
        if self.head:
            self.head.prev=None
        return self.head
    def delete_last(self):
        if self.head==None:
            print("Empty list")
            return
        if self.head.next==None:
            self.head=None
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        last=curr.prev
        last.next=None
        return self.head
    def delete_at(self,pos):
        if self.head==None:
            print("Empty list")
            return
        
        if pos==0:
            self.delete_head()
            return
        curr=self.head
        c=0
        while curr and c<pos:
            curr=curr.next
            c+=1
        if not curr:
            print("Out of bounds")
            return
        curr.prev.next=curr.next
        if curr.next:
            curr.next.prev=curr.prev
        return self.head

dl=doubleLL()
dl.traverse()
a=input("Enter 1st node = ")
dl.insert_at_head(a)
dl.traverse()
n=int(input("Enter rest number of nodes = "))
for i in range(n):
    val=input("Enter node value = ")
    dl.append(val)
dl.traverse()
p=int(input("For random insert enter position = "))
b=input("Enter node value = ")
dl.insert_at(b,p)
dl.traverse()
dl.delete_head()
dl.traverse()
dl.delete_last()
dl.traverse()
ve=int(input("Enter position to delete = "))
dl.delete_at(ve)
dl.traverse()