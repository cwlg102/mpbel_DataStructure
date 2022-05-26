#BinarySearchTree...
import time
from collections import deque
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
         #출력을 위한 노드마다의 검사할 변수

class BinaryTree:
    def __init__(self, data=None):
        self.root = TreeNode(data)

    def Insert(self, node, insdata):
        if node == None: #종료조건
            node = TreeNode(insdata, None, None)
            
        elif node.data > insdata:
            node.left = self.Insert(node.left, insdata) #return값이 있으므로 연결지어줘야...
            
        elif node.data < insdata:
            node.right = self.Insert(node.right, insdata)
            
        else:
            pass
        
        return node

    #직접 자신을 체크하며
    def PreOrder(self, node):
        if node == None:
            return 
        else:
            print(node.data)
            self.PreOrder(node.left)
            self.PreOrder(node.right)

    #자식 노드를 확인하며        
    def BFS(self, root):
        queue = deque() #리스트로도 구현 가능
        queue.append(root)
        while queue:
            node = queue.popleft()
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    def DeleteLeaf(self):
        queue = deque() #리스트로도 구현 가능
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            #node를 직접 None으로 지정하면, 해당 노드를 가리키고있는 부모노드는 
            #해당 노드의 정보를 가지고 있어서 지워지지 않는것으로 생각됨... 
            #따라서 조금 번거롭지만 다음과 같은 방식으로 해봤음
            delflag = 0
            if node.left:
                if node.left.left == None and node.left.right == None:
                    node.left = None
                    delflag = 1
                if not delflag:    #여기서 continue를 걸어버리면 오른쪽 확인을 못함
                    queue.append(node.left)
                
            if node.right:
                if node.right.left == None and node.right.right == None:
                    node.right = None 
                    continue #왼오 다확인했으므로 continue 걸어도됨
                
                queue.append(node.right)
            
    def Visualization(self, node):
        if node.left == None and node.right == None:
            return
        elif node.left != None and node.right == None:
            print(node.data,'의 자식: ',node.left.data)
            self.Visualization(node.left)
        elif node.left == None and node.right != None:  
            print(node.data,'의 자식: ', node.right.data)
            self.Visualization(node.right)  
        else:
            print(node.data,'의 자식: ',node.left.data, node.right.data)
            self.Visualization(node.left)
            self.Visualization(node.right)
            

start = time.time()           
b = BinaryTree(45)

b.Insert(b.root,15)
b.Insert(b.root,48)
b.Insert(b.root,46)
b.Insert(b.root,21)
b.Insert(b.root,231)
b.Insert(b.root,234)
b.Insert(b.root,85)
b.Insert(b.root,100)
b.Insert(b.root,49)
b.Insert(b.root,4)
b.Insert(b.root, 1)
b.Insert(b.root, 22)
b.Insert(b.root, -2)
b.Insert(b.root, 5)
b.PreOrder(b.root)
b.Visualization(b.root)
print()
b.BFS(b.root)
print()
b.DeleteLeaf()
b.BFS(b.root)
print()
b.DeleteLeaf()
b.BFS(b.root)
print(time.time()-start)