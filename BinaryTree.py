class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
     
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
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

def inOrderTraversal(root):
    if root is None:
        return
    else:
        inOrderTraversal(root.left)
        print(root.data, end=' ')
        inOrderTraversal(root.right)

def preOrderTraversal(root):
    if root is None:
        return
    else:
        print(root.data, end=' ')
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

def postOrderTraversal(root):
    if root is None:
        return
    else:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.data, end=' ')

if __name__ == '__main__':
    print('Binary tree')

    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')
    
# inOrderTraversal(root)
# preOrderTraversal(root)
postOrderTraversal(root)
