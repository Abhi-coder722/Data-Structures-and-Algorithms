class stackarray:
    def __init__(self):
        self.stack=[]
    def push(self,e):
        self.stack.append(e)
    def pop(self):
        if self.isEmpty():
            print("Already the stack is empty...")
            return
        else:
            last=self.stack[-1]
            del(self.stack[-1])
            return last
    def isEmpty(self):
        if self.stack[0] is None:
            return True
        else:
            return False

    def peek(self):
        return self.stack[0]

    def display(self):
        print(self.stack)
s=stackarray()
s.push(11)
s.push(16)
s.push(15)
s.display()
print(s.peek())

print("Poping out elements one by one ::::::: ")

print(s.pop())
print(s.pop())
print(s.pop())