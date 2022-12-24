#creating a node 
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        
#Circular - Singly - Linked List        
class CSLL:
    def __init__(self):
        self.head=None
        self.next=None
        
    #adding element at the beginning of the Circular Linked List
    def addbeg(self,data):
        nn=Node(data)
        if self.head is None:
            self.head=nn
            nn.next=self.head
        else:
            n=self.head
            while n.next is not self.head:
                n=n.next
            n.next = nn
            nn.next = self.head
            self.head=nn

    #adding element at the end of the Circular Linked List            
    def addend(self,data):
        nn=Node(data)
        n=self.head
        if self.head is None:
            self.head=nn
            nn.next=self.head
        else:
            while n.next is not self.head:
                n=n.next
            t=n.next
            n.next=nn
            nn.next = t
            
            
    #adding element at a specified position beginning of the Circular Linked List            
    def addmid(self,data,pos):

        n=self.head
        if self.head is None:
            nn=Node(data)
            self.head=nn
            nn.next=self.head
        else:
            i=1
            while i < pos:
                n=n.next
                i+=1
            if n.next == self.head:
                self.addend(data)
                return
            else:
                nn=Node(data)
                t=n.next
                n.next=nn
                nn.next=t
                
    #deleting an element from the beginnig
    def delbeg(self):
        n=self.head
        if n is None:
            print("The list is empty..")
            return
        else:
            t=n.next
            while n.next is not self.head:
                n=n.next
            n.next=t
            self.head = t
            
    #deleting an element from the end 
    def delend(self):
        n=self.head
        if n is None:
            print("The list is empty..")
        if (n.next.next is self.head):
            n.next=self.head
        else:
             while n.next.next is not self.head:
                 n=n.next
             n.next=self.head
            
#    Traversing through the list 
    def traverse(self):
        temp=self.head
        if self.head is not None:
            while(True):
                print(temp.data, end = " ")
                temp = temp.next
                if (temp == self.head):
                    break
    
c=CSLL()
c.addbeg(55)

print("After adding the first element:")
c.traverse()
print()
c.addbeg(19)
c.addbeg(97)
c.addbeg(15)
print("After adding the elements")
c.traverse()

c.addend(57)
print("After adding the element at the end::: ")
c.traverse()

c.addmid(2,2)
print("\nAfter adding the element at the specified position::: ")
c.traverse()

c.delbeg()
print("\nAfter deleting from the beginning:")
c.traverse()
      
c.delend()
print("\nAfter deleting from the end:")
c.traverse()
