class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class doble():
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
        new.prev=curr
    def trav(self):
        if self.head==None:
            print("Empty List")
            return
        curr=self.head
        while curr:
            print(curr.val,end=" ")
            curr=curr.next
        print()
    def pairsumbrute(self,tar):
        lis=[]
        temp1=self.head
        while temp1:
            temp2=temp1.next
            while temp2:
                if temp1.val+temp2.val==tar:
                    lis.append([temp1.val,temp2.val])
                temp2=temp2.next
            temp1=temp1.next
        return lis
    def pairsumset(self,key):
        my_Set=set()
        temp=self.head
        res=[]
        while temp:
            rem=key-temp.val
            if rem in my_Set:
                res.append([rem,temp.val])
            my_Set.add(temp.val)
            temp=temp.next
        return res
    def pairsumoptimal(self,key):
        res=[]
        left=self.head
        right=self.head
        while right.next:
            right=right.next
        while left is not None and right is not None and left.val<right.val:
            total=left.val+right.val
            if total == key:
                res.append([left.val,right.val])
                left=left.next
                right=right.prev
            elif total>key:
                right=right.prev
            else:
                left=left.next
        return res
dub=doble()
n=int(input("Enter number of nodes = "))
for i in range(n):
    val=int(input("Enter node val = "))
    dub.append(val)
k=int(input("Enter value to be summed = "))
if dub.pairsumbrute(k):
    print("Linked List contains pair of",k,"as",dub.pairsumbrute(k))
else:
    print("No pairs found")        
if dub.pairsumset(k):
    print("Linked List contains pair of",k,"as",dub.pairsumset(k))
else:
    print("No pairs found")  
if dub.pairsumoptimal(k):
    print("Linked List contains pair or",k,"as",dub.pairsumoptimal(k))
else:
    print("No pairs found")