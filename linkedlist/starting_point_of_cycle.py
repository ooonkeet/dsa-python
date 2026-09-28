class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class singli():
    def __init__(self):
        self.head=None
    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
    def traverse(self):
        if self.head==None:
            print("List is empty")
            return
        curr=self.head
        while curr is not None:
            print(curr.val,end=" ")
            curr=curr.next
        print()
    def createcycle(self,pos):
        if pos==-1:
            return
        curr=self.head
        cycl_nod=None
        c=0 #for 0 based indexing set c=0 and for 1 based indexing set c=1
        while curr.next:
            if c==pos:
                cycl_nod=curr
            curr=curr.next
            c+=1
        if c==pos:
            cycl_nod=curr
                
        curr.next=cycl_nod
    def cycl_brute(self):
        temp=self.head
        myS=set()
        while temp is not None:
            if temp in myS:
                return temp
            myS.add(temp)
            temp=temp.next
        return None
    def cycl_optm(self):
        slow=self.head
        fast=self.head
        while fast!=None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=self.head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
sl=singli()
n=int(input("Enter number of nodes = "))
for i in range(n):
    v=input("Enter value of node = ")
    sl.append(v)
pos=int(input("Enter position to create cycle (-1 for no cycle, 0-based indexing) = "))
sl.createcycle(pos)
if sl.cycl_brute():
    print("The starting point of cycle is = ",sl.cycl_brute().val)
else:
    print("There is no cycle")
if sl.cycl_optm() is not None:
    print("The starting point of cycle is = ",sl.cycl_optm().val)
else:
    print("There is no cycle")