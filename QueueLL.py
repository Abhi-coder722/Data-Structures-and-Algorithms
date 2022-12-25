class Node:
    def __init__(self,d):
        self.d=d
        self.next=None
class queueLL:
    def __init__(self):
        self.r=None
        self.f=None

    def enqueue(self,x):
        newn=Node(x)
        if self.r is None:
            self.f=self.r=newn
            return
        self.r.next=newn
        self.r=newn
    def dequeue(self):
        if self.r is None:
            print('Empty queue..')
        elif self.r==self.f:
            self.r=self.f=None
        else:
            self.f=self.f.next
    def display(self):
        t=self.f
        while t is not self.r :
            print(t.d)
            t=t.next
q=queueLL()
q.enqueue(55)
q.enqueue(65)
q.enqueue(75)
q.enqueue(95)
q.enqueue(0)
print('Initial queue after enqueue....')
q.display()
q.dequeue()
print('Initial queue after dequeue....')
q.display()
