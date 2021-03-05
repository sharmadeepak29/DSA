class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right= None


class BST:
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def remove(self, val , parentNode = None):
        pass

    def search(self, val):
        pass

def printInorder(root:Node):
    if root == None:
        return
    else:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def findInorderSuccessor(root, val):
    if root == None:
        return

    if root.val == val:
        if root.right is not None:
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            findInorderSuccessor.suc = tmp

    if root.val > val:
        findInorderSuccessor.suc = root
        findInorderSuccessor(root.left, val)
    else:
        findInorderSuccessor(root.right, val)


Tree = BST()
Tree.insert(50)
Tree.insert(30)
Tree.insert(20)
Tree.insert(40)
Tree.insert(70)
Tree.insert(60)
Tree.insert(80)
printInorder(Tree.root)
findInorderSuccessor.suc = None
findInorderSuccessor(Tree.root, 50)
if findInorderSuccessor.suc is not None:
    print("Successor is:",findInorderSuccessor.suc.val)
