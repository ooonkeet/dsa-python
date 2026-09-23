class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class single():
    def __init__(self):
        self.head=None
    def append(self,val):
        new=Node(val)
        if self.head == None:
            self.head=new
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new
    def traverse(self):
        if self.head==None:
            print("Empty list")
            return
        curr=self.head
        while curr is not None:
            print(curr.val,end=" ")
            curr=curr.next
        print()
    def cyclbruteforce(self):
        temp=self.head
        my_set=set()
        while temp!=None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp=temp.next
        return False
    def cycloptimiz(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    def createcycle(self,pos):
        if pos==-1:
            return
        curr=self.head
        cycl_nod=None
        count=1 #for 0 based indexing set c=0 and for 1 based indexing set c=1
        while curr.next:
            if count==pos:
                cycl_nod=curr
            curr=curr.next
            count+=1
        if count==pos:
            cycl_nod=curr
        curr.next=cycl_nod
sl=single()
n=int(input("Enter number of nodes = "))
for i in range(n):
    v=input("Enter value of node = ")
    sl.append(v)
pos=int(input("Enter position to create cycle (-1 for no cycle, 1-based indexing) = "))
sl.createcycle(pos)
if sl.cyclbruteforce():
    print("Cycle detected")
else:
    print("No cycle")
if sl.cycloptimiz():
    print("Cycle detected")
else:
    print("No Cycle")