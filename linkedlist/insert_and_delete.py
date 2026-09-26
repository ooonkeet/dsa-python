class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def append(self,val):
        new_nod=Node(val)
        if self.head==None:
            self.head=new_nod
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_nod
    def traverse(self):
        if self.head==None:
            print("Empty List")
        else:
            curr=self.head
            while curr:
                print(curr.val,end=" ")
                curr=curr.next
            print()  
    def insert_at(self,val,pos):
        new_nod=Node(val)
        if pos==0:
            new_nod.next=self.head
            self.head=new_nod
        else:
            curr=self.head
            prev_node=None
            count=0
            while curr and count<pos:
                prev_node=curr
                curr=curr.next
                count+=1
            if count != pos:
                print("Invalid position")
                return
            prev_node.next=new_nod
            new_nod.next=curr  
    def delete(self, val):
        temp = self.head

        if temp == None:
            print("Empty List")
            return

        if temp.val == val:
            self.head = temp.next
            return

        prev = None

        while temp:
            if temp.val == val:
                prev.next = temp.next
                return

            prev = temp
            temp = temp.next

        print("Node not found")
sl=single()
n=int(input("Enter number of nodes you want = "))
for i in range (n):
    v=input("Enter value of node = ")
    sl.append(v)
sl.traverse()
sl.insert_at("trincas",2)
sl.traverse()
val=input("Enter value of node to delete = ")
sl.delete(val)
sl.traverse()