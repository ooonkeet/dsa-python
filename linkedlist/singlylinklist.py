class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
            # while current.next is not None:
                current=current.next
            current.next=new_node
    def traverse(self):
        if self.head==None:
            print("List is empty")
        else:
            current=self.head
            while current:
                print(current.val,end=" ")
                current=current.next
            print() #for new line after printing all values

sll=SinglyLinkedList()
sll.traverse() #prints List is empty

n=int(input("Enter number of nodes to be created: "))
for i in range(n):
    val=int(input("Enter value of node: "))
    sll.append(val)
sll.traverse() #prints all values of nodes in the linked list