#doubly linked list........

#It is a collection od nodes containing the three parts
#namely data part, previous node's address and the next node's address.....



#creating a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    #adding element at the beginning of the doubly linked list
    def addbeg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            
    #traversing the list i.e. reading elements from the list
    def traverse(self):
        if self.head is None:
            print("The list is empty..")
        else:
            n=self.head
            while n is not None:
                print(str(n.data)+"  ",end="")
                n=n.next
    
    #adding element at the end 
    def addend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            
    #Deleting the first element from the list
    def delbeg(self):
        if self.head is None:
            print("The list is empty...")
            return
        else:
            t=self.head
            self.head=t.next
            self.head.prev=None
            del(t)
            
    #Deleting the last element from the list
    def delend(self):
        if self.head is None:
            print("The list is empty...")
            return
        else:
            t=self.tail
            t.prev.next=None
            del(t)
            
    #inserting the element at a specified position in the list
    def inspos(self,data,posi):
        new_node=Node(data)
        n=self.head
        i=1
        while i<posi-1 :
            i+=1
            n=n.next
        new_node.prev=n
        new_node.next=n.next
        n.next.prev=new_node
        n.next=new_node
        
    #deleting the element from a specified position in the list
    def delpos(self,pos):
        if self.head is None:
            print("The list is empty...")
            return
        else:
            n=self.head
            i=1
            while(i < pos-1):
                i+=1
                n=n.next
            n.next=n.next.next
            n.next.prev=n
            
            
            
 # all the above operations can be performed 
c=DLL()
c.addbeg(38)
c.addbeg(45)
c.addbeg(5)
c.addbeg(62)
c.addbeg(48)
c.addbeg(15)
c.addbeg(99)
c.traverse()
print("\n after adding at end...")
c.addend(55)
print("\nAfter deleting from the beginning..")
c.delbeg()
c.traverse()
print("\nAfter deleting from the end..")
c.delend()
c.traverse()

print("\nAfter deleting from the position.")
c.delpos(2)
c.traverse()
print("\ninsertion posi")
c.inspos(1555,3)
c.traverse()
