class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node1.next=node2
node2.next=node3
node3.next=node4

print(node1) #prints address of node1
print(node1.val) #prints value of node1
print(node1.next) #prints address of node2 which is next of node1
print(node2) #prints address of node2
print(node2.val) #prints value of node2