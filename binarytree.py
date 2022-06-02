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
    def PreOrderDFS(self, node):
        if node == None:
            return 
        else:
            print(node.data)
            self.PreOrderDFS(node.left)
            self.PreOrderDFS(node.right)

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
            if node.left: #왼쪽 자식 존재할 시
                if node.left.left == None and node.left.right == None: #왼쪽자식의 왼쪽이 없고 왼쪽자식의 오른쪽이없다면
                    node.left = None #왼쪽자식이 리프노드이므로, 왼쪽 자식 삭제
                    delflag = 1 #삭제 플래그
                if not delflag: #왼쪽 자식노드가 또 다른 자식노드를 가지고있다는 것. 즉, 리프노드가 아니라는것
                    #여기서 continue를 걸어버리면 오른쪽 확인을 못함
                    queue.append(node.left)
                
            if node.right: #오른쪽 자식 존재할 시
                if node.right.left == None and node.right.right == None: #오른쪽 자식의 오른쪽이 없고 오른쪽자식의 왼쪽이 없다면
                    node.right = None  #오른쪽 자식 삭제
                    continue #왼오 다확인했으므로 continue 걸어도됨
                #continue에 걸리지 않았다면 if문에 걸리지 않은거고 이는 곧 오른쪽자식이 리프노드가 아니라는것.
                queue.append(node.right) 
            
    def Visualization(self, node):
        if node.left == None and node.right == None: #왼쪽자식, 오른쪽 자식이 없다면 리프노드임
            print(node.data,'is 리프노드')
            return
        elif node.left != None and node.right == None: #오른쪽 자식은 없고 왼쪽자식만 있을시...
            print(node.data,'의 자식: ',node.left.data)
            self.Visualization(node.left)
        elif node.left == None and node.right != None: #왼쪽 자식은 없고 오른쪽 자식만 있을시... 
            print(node.data,'의 자식: ', node.right.data)
            self.Visualization(node.right)  
        else: #둘 다 자식이 있을 시...
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
b.PreOrderDFS(b.root)
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