#creating node
class Node:
     def __init__ (self,data):
         self.data=data
         self.ref=None
node1 = Node(10)
print(node1)


#traversal oper.
#if list is empty
class LinkedList:
    def __init__(self):
        self.head=None
        self.ref=None

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    # adding after a node 
    def add_after (self,data,x):
        n=self.head
        while n is not None :
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("The node isn't present")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node  
 
    # adding before a specific node             
    def add_before(self,data,x):
        if self.head is None:
            print("The Linked List is absent")
            return

        if self.head.data ==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head

        while n.ref is not None:
            if(n.ref.data==x):
                break
            n=n.ref

        if n.ref is None:
            print("Node is absent")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node


    def add_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("The linked list is not empty")

    def removal_begin(self):
        n=self.head
        if n is not None:
            self.head=n.ref
        else:
            print("Linked list is empty so we can't delete nodes")

    def removal_end(self):
         if self.head is None:
            print("Linked list is empty so we can't delete nodes")
         elif self.head.ref is None:
             self.head=None
         else:
            n=self.head
            while n.ref.ref is not None:
                n.ref
            n.ref=None

    def removal_by_value(self,x):
        if(self.head is None):
            print("LL is empty")
            return
        if self.head.data ==x :
            self.head=self.head.ref
            return
        
        n=self.head
        while n.ref is not None :
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is absent")
        else:
            n.ref=n.ref.ref

    def search_ll(self,data):
        if self.head==None:
            print("Empty.")
        else:
            n=self.head
            while n is not None:
                c=0
                if(data==n.data):
                    c=c+1
                    print("The number is found..")
                n=n.ref
            if(c==0):
                print("The number isnt present")
    def count_ll(self):
        c=0
        n=self.head
        if n==None:
            print("Empty: ")
        while n is not None:
            c=c+1
            n=n.ref
        print("Count is : ",c)


    def reverseList(self):
          previous = None
          current = self.head     
          nextn = self.head    
          while current is not None:
               nextn=current.ref
               current.ref=previous
               previous=current
               current=nextn
          self.head=previous

    def print_LL(self):
        if(self.head == None):
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"----->",end="  ")
                n=n.ref



# We can perform all the operations mentioned above 
LL1=LinkedList()
LL1.add_begin(5)
LL1.add_begin(4)
LL1.add_begin(9)
LL1.add_begin(8)

LL1.print_LL()

print("\nAFTER REVERSE")
LL1.reverseList()
LL1.print_LL()