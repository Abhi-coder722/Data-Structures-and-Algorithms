class node:
    def __init__(self,data):
        self.data=data
        self.top=None
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        self.next=None
    def push(self,data):
        global t
        nn=node(data)
        if self.top is None:
            self.top=nn
            t+=1
            return
        else:
            nn.next=self.top
            self.top=nn
            t+=1
            return


    def pop(self):
        global t
        if self.top is None:
                print("Empty stack....")
                return None
        else:
                tem=self.top
                self.top=self.top.next
                t-=1
                return tem.data
    def display(self):
            tem=self.top
            if tem is None:
                print("Empty stack...")
                return
            while tem is not None:
                print(tem.data," -->")
                tem=tem.next
                
    def peek(self):
            if self.top is None:
                print("The stack is empty........")
                return None
            else:
                return self.top.data
    def isEmpty(self):
            if t<0 :
                return True
            else:
                return False

    def merge(self,l1,l2):
        if l1.data>l2.data:
            mergel=l2.data
        else:
            mergel=l1.data
        while l1 != None& l2 != None :
            if l1.data < l2.data:
                mergel.next=l1
                l1=l1.next
            else:
                mergel.next=l2
                l2=l2.next
        return mergel

MyStack = Stack()
 
MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)


MyStack1 = Stack()
 
MyStack1.push(10)
MyStack1.push(25)
MyStack1.push(3)
MyStack1.push(94)
X=Stack()

# Display stack elements
MyStack.display()
 
# Print top element of stack
print("\nTop element is ",MyStack.peek())
print("after poping two elements using LIFo technique of stack..")
# Delete top elements of stack
MyStack.pop()
MyStack.pop()
 
# Display stack elements
MyStack.display()
 
# Print top element of stack
print("\nTop element is ", MyStack.peek())
print('stack is : ')
MyStack.display()
print('Empty stack :: ',MyStack.isEmpty())