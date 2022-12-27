class bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return 
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=bst(data)
    def search(self,data):
        if self.key == data:
            print('The node is found')
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('The node is not found')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('The node is not found')
    def preorder(self):
        print(self.key,end='   ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def inorder(self):
        if self.lchild:
            self.lchild.preorder()
        print(self.key,end='   ')
        if self.rchild:
            self.rchild.preorder()
    def postorder(self):
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
        print(self.key,end='   ')
    def delete(self,data):
        if (self.lchild and self.rchild is None) and self.key is data:
            print('Cannot delete single node..')
        if self.key is None:
            print('Empty tree No deletions can be performed ')
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print('\nThe node is absent !')
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print('\nThe node is absent !')
        else:
                if self.lchild is None:
                    temp=self.rchild
                    self=None
                    return temp
                if self.rchild is None:
                    temp=self.lchild
                    self=None
                    return temp
                small=self.rchild
                while small.lchild:
                    small=small.lchild
                self.key=small.key
                self.rchild=self.rchild.delete(small.key)
        return self
    
r=bst(15)

print('\nPre order traversal algorithm..')
r.preorder()
print('\nIn order traversal algorithm..')
r.inorder()
print('\nPost order traversal algorithm..')
r.postorder()
r.delete(15)
print('\nPre order traversal algorithm after deleting the root node ..')
r.preorder()