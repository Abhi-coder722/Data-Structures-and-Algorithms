class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        self.prev=None
class CDLL:
    def __init__(self):
        self.head=None
        self.next=None
        self.prev=None
        
    def addbeg(self,data):
        nn=Node(data)
        n=self.head
        if n is None:
            self.head=nn
            nn.next=nn
            nn.prev=nn
        else:
            while n.next is not self.head:
                n=n.next
            self.head.prev=nn
            nn.next=self.head
            self.head=nn
            nn.prev=n
            n.next=nn
    def addend(self,data):
        nn=Node(data)
        n=self.head
        if(n is None):
            self.head=nn
            nn.next=nn
            nn.prev=nn
            return
        else:
            while n.next is not self.head:
                n=n.next
            nn.prev=n
            n.next=nn
            nn.next=self.head
            self.head.prev=nn
    def addpos(self,data,pos):
        n=self.head
        if(n is None):
            nn=Node(data)
            self.head=nn
            nn.next=nn
            nn.prev=nn
            return
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
                n.next.prev=nn
                nn.prev=n
                n.next=nn
                nn.next=t
    def delbeg(self):
        n=self.head
        if n is None:
            print("\nEmpty list .... ")
            return
        else:
            while(n.next is not self.head):
                n=n.next
            n.next=self.head.next
            self.head=self.head.next
            self.head.prev=n
    def delend(self):
        n=self.head
        if n is None:
            print("\nEmpty list .... ")
            return
        else:
            while(n.next.next is not self.head):
                n=n.next
            n.next=self.head
            self.head.prev=n
    def traverse(self):
        temp=self.head
        if self.head is not None:
            while(True):
                print(temp.data, end = " ")
                temp = temp.next
                if (temp == self.head):
                    break
c=CDLL()
c.addbeg(5)
print("After adding the first element")
c.traverse()
c.addbeg(19)
c.addbeg(4)
c.addbeg(15)
c.addbeg(11)
print("The douby circular linked list is as follows: ")
c.traverse()

print("\nAfter adding the element at the end :: ")
c.addend(444)
c.traverse()

c.addpos(22,3)
print("\nThe douby circular linked list is as follow after adding at specified position..: ")
c.traverse()

c.delbeg()
print("\nAfter deleting the first element ..:")
c.traverse()

c.delend()
print("\n After deleting the last element:")
c.traverse()