class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        if self is not None:
            self.left.inorder() if self.left else None
            print(str(self.data) + "->", end=' ')
            self.right.inorder() if self.right else None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    ''' Deletion
    1. If the node to be deleted is a leaf node, then in such case we can simply delete the node.
    2. If the node to be deleted has a single child node, In such case :
        a. Replace that node with its child node.
        b. Removes the child node from its original position
    3. If the node to be deleted has two children, In such case :
        a. Get the inorder successor of that node.
        b. Replace the node with the inorder successor.
        c. Remove the inorder successor from its original position.
    '''

    def deletenode(self, data):
        if self is None:
            return None
        if data < self.data:
            self.left = self.left.deletenode(data) if self.left else None
        elif data > self.data:
            self.right = self.right.deletenode(data) if self.right else None
        else:
            if self.left is None:
                temp = self.right
                self.right = None
                return temp
            if self.right is None:
                temp = self.left
                self.left = None
                return temp
            temp = self.find_min(self.right)
            self.data = temp.data
            self.right = self.right.deletenode(temp.data) if self.right else None
        return self
    
    def findval(self,value):
        if value < self.data:
            if self.left is None:
                return str(value)+" Not Found"
            return self.left.findval(value)
        elif value > self.data:
            if self.right is None:
                return str(value)+ " Not Found"
            return self.right.findval(value)
        else:
            print(str(self.data)+ ' is found')


# Example usage:
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.deletenode(12)
print(root.findval(14))
print(root.findval(7))
print("--------Inorder traversal--------")
root.inorder()
