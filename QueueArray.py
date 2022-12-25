class queueArray:
    # //queue data structure implemeneted in python
    def __init__(self,s):
        self.q=[]
        self.r=-1
        self.f=-1
        self.s=s
        
    def enqueue(self,x):
        if self.r==self.s:
            print('The queue is full..')
            return
        elif self.r and self.f == -1:
            self.q.append(x)
            self.r+=1
            self.f+=1
        else:
            self.q.append(x)
            self.r+=1
    def dequeue(self):
        if self.r and self.f == -1:
            print('Empty queue')
        elif self.f==self.r:
            self.f=-1
            self.r=-1
        else:
            x=self.q[self.f]
            del(self.q[self.f])
            self.f+=1
            return x
    def display(self):
        if self.r and self.f == -1:
            print('Empty queue')
        else:
            for i in self.q:
                print(i)
q=queueArray(5)
q.enqueue(22)
q.enqueue(55)
q.enqueue(33)
q.enqueue(12)
print('Queue after enqueue..')
q.display()

print('Queue after dequeue..',q.dequeue())
q.display()