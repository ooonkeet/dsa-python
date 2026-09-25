class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class singlu:
    def __init__(self):
        self.head=None
    def append(self,val):
        newNode=Node(val)
        if self.head==None:
            self.head=newNode
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=newNode
    def traverse(self):
        if self.head==None:
            print("List is empty")
            return
        curr=self.head
        while curr is not None:
            print(curr.val,end=" ")
            curr=curr.next
        print()
    def createCycle(self,pos):
        if pos==-1:
            return
        curr=self.head
        cycl=None
        count=0
        while curr.next:
            if count==pos:
                cycl=curr
            curr=curr.next
            count+=1
        if count==pos:
            cycl=curr
        curr.next=cycl
    def lengloop_brute_force(self):
        temp=self.head
        trav=0
        my_dic=dict() # or my_dic={}
        while temp is not None:
            if temp in my_dic:
                return trav-my_dic[temp]
            my_dic[temp]=trav
            trav+=1
            temp=temp.next
        return None
    def lengloop_optm(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=slow.next
                trav=1
                while slow!=fast:
                    trav+=1
                    slow=slow.next
                return trav
        return None
sl=singlu()
n=int(input("Enter number of nodes = "))
for i in range(n):
    v=input("Enter value of node = ")
    sl.append(v)
pos=int(input("Enter position to create cycle (-1 for no cycle, 0-based indexing) = "))
sl.createCycle(pos)
if sl.lengloop_brute_force():
    print("Length of loop =",sl.lengloop_brute_force())
else:
    print("No cycle present")
if sl.lengloop_optm():
    print("Length of loop =",sl.lengloop_optm())
else:
    print("No cycle present")