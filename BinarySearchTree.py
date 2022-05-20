#BinarySearchTree...
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.nodestatus = 0 #출력을 위한 노드마다의 검사할 변수

class BinaryTree:
    def __init__(self, data):
        self.root = TreeNode(data)

    #디버깅 상으로는 정확하게 들어감(같은 값 없다는 가정 하에)
    #같은 것은 들어갈 수 없음
    #숫자에 한하여 가능함
    def Insert(self, insdata):
        insnode = TreeNode(insdata)
        node = self.root
        while(1): #같을 시 루프 빠져나감!
            if node.left == None and node.right ==None: #둘다 None일때(리프노드 도착)
                if insdata > node.data:
                    node.right = insnode
                elif insdata < node.data:
                    node.left = insnode
                break
            elif node.left == None and node.right != None: #왼쪽자식만 None일때
                if insdata > node.data:
                    node = node.right
                elif insdata < node.data:
                    node.left = insnode
                    break
                else:
                    break
            elif node.right == None and node.left != None: #오른쪽자식만 None일때
                if insdata > node.data:
                    node.right = insnode
                    break
                elif insdata < node.data: 
                    node = node.left
                else:
                    break
            else: #둘다 None이 아닐때
                if insdata > node.data: 
                    node = node.right
                elif insdata < node.data:
                    node = node.left
                else:
                    break

    def Search(self, srcdata):
        node = self.root
        switch = 0
        while node.left != None or node.right != None:
            if srcdata < node.data:
                node = node.left
            elif srcdata > node.data:
                node = node.right
            else:
                print('Find')
                switch = 1
                break  

    def PreOrder(self, node):
        if node.nodestatus == 0:
            print(node.data)
            node.nodestatus = 1
            if node.left != None:
                self.PreOrder(node.left)
    
            if node.right != None:
                self.PreOrder(node.right)
            
        else:
            pass
            
        
        
            

            
bst = BinaryTree(45)
bst.Insert(15)
bst.Insert(46)
bst.Insert(46)
bst.Insert(21)
bst.Insert(231)
bst.Insert(79)
bst.Insert(90)
bst.Insert(47)
bst.Insert(4)
bst.PreOrder(bst.root)



            


        