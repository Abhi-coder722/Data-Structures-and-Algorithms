class conversion:
    def __init__(self):
        self.top=-1
        self.array=[]
        self.output=[]
        self.precedence={'1':'+','1':'-','2':'*','2':'/','3':'^'}
    def push(self,i):
        self.array.append(i)
        self.top+=1
    def pop(self):
        if self.top ==-1:
            return
        self.top-=1
        return self.array.pop()
    def peek(self):
        return self.array[-1]
    def isEmpty(self):
        return True if self.top ==-1 else False
    def isOperand(self,i):
        return i.isalpha()
    def notgreater(self,i):
        try:
            a=self.precedence[i]
            b=self.precedence[self.peek()]
            return True if a<=b else False
        except KeyError:
            return False
    def infixtopostfix(self,exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i =='(':
                self.push(i)
            elif i==')':
                while (not self.isEmpty()) and self.peek() !='(':
                    self.output.append(self.pop())
                self.pop()
            else:
                while (not self.isEmpty()) and self.notgreater(i):
                    if i=='^' and self.array[-1]==i:
                        break
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
                self.output.append(self.pop())
        print(''.join(self.output))
exp = "(A+B)*C+(D-E)/F+G"
obj = conversion()
obj.infixtopostfix(exp)