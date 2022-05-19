############################Doubly Linked List############################
class Node: #DLL에서 노드 클래스는 데이터 객체와 비어있는 이전 객체, 비어있는 다음값 객체로 주어짐
    def __init__(self, data, prev=None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self, data='boundary'): #기준머리와 꼬리를 잡아줌
        self.headdummyNode = Node(data)
        self.taildummyNode = Node(data)
        self.headdummyNode.next = self.taildummyNode
        self.taildummyNode.prev = self.headdummyNode
        self.num = 0 #Add, Insert 할 때 +1, Delete 할 때 -1

    def AddTail(self, data):  
        tailnode = Node(data)
        tailnode.prev = self.taildummyNode.prev #(끝에 넣고자하는 노드)의 prev를 (꼬리 더미 노드의 전에있던) 노드를 가리키게 함
        tailnode.next = self.taildummyNode #(끝에 넣고자하는 노드)의 next를 (꼬리 더미 노드)를 가리키게 함
        self.taildummyNode.prev.next = tailnode #(꼬리 더미 노드의 전에있던) 노드의 next를 (끝에 넣고자하는 노드)를 가리키게 함
        self.taildummyNode.prev = tailnode #(꼬리 더미 노드)의 prev를 (끝에 넣고자하는 노드)를 가리키게 함
        self.num += 1

    def AddHead(self, data): 
        headnode = Node(data)
        headnode.next = self.headdummyNode.next #(앞에 넣고자하는 노드)의 next를 (머리 더미 노드의 후에 있던) 노드를 가리키게 함
        headnode.prev = self.headdummyNode #(앞에 넣고자하는 노드)의 prev를 (머리 더미 노드)를 가리키게 함
        self.headdummyNode.next.prev = headnode #(머리 더미 노드 후에 있던) 노드의 prev를 (앞에 넣고자하는 노드)를 가리키게 함
        self.headdummyNode.next = headnode #(머리 더미 노드)의 next를 (앞에 넣고자하는 노드)를 가리키게 함
        self.num += 1

    def InsertNode(self, pivotdata, data):
        ins_node = Node(data)
        n_node = self.headdummyNode
        p_node = self.taildummyNode 
        #n_node는 머리에서 꼬리로 p_node는 꼬리에서 머리로 오면서 pivotdata를 검사
        #둘중 먼저 발견하는 쪽에서, 값을 삽입
        while n_node.next != None and p_node.prev != None:
            
            if n_node.data == pivotdata:
                ins_node.prev = n_node #AddHead나 AddTail과 같은 논리.
                ins_node.next = n_node.next
                n_node.next.prev = ins_node
                n_node.next = ins_node
                self.num += 1
                break
            
            if p_node.data == pivotdata:
                ins_node.prev = p_node
                ins_node.next = p_node.next
                p_node.next.prev = ins_node
                p_node.next = ins_node
                self.num += 1
                break
    
            n_node = n_node.next
            p_node = p_node.prev    

    def DeleteNode(self, deldata):
        n_node = self.headdummyNode
        p_node = self.taildummyNode
        #n_node는 머리에서 꼬리로 p_node는 꼬리에서 머리로 오면서 deldata를 검사
        #지울 노드의 전 노드 next를 지울 노드의 후 노드를 가리키게
        #지울 노드의 후 노드 prev를 지울 노드의 전 노드를 가리키게
        while n_node.next != None and p_node.prev != None:
            if n_node.data == deldata: #deldata를 먼저 발견한 쪽에서 삭제
                n_node.prev.next = n_node.next 
                n_node.next.prev = n_node.prev
                self.num -= 1
                break
            if p_node.data == deldata:
                p_node.prev.next = p_node.next
                p_node.next.prev = p_node.prev
                self.num -= 1
                break

            n_node = n_node.next
            p_node = p_node.prev

    def SearchNode(self, srcdata):
        n_node = self.headdummyNode
        p_node = self.taildummyNode
        idx = -1
        switch = 0
        while n_node.next != None and p_node.prev != None:
            idx += 1
            if n_node.data == srcdata:
                print('Find!!!:', idx-1)
                switch = 1
                break

            if p_node.data == srcdata:
                print('Find!!!:', self.num - idx)
                switch = 1
                break
            
            n_node = n_node.next
            p_node = p_node.prev
        if switch == 0:
            print('찾는 값 없음')
        



dll = DoublyLinkedList()
dll.AddHead(4)
dll.AddHead(100)
dll.AddHead(512)
dll.AddTail(321)
dll.AddTail(9090)
dll.InsertNode(321, 'ㅇ')
dll.DeleteNode(9)
node = dll.headdummyNode

while node.next:
    print(node.data)
    node = node.next
print(node.data)

dll.SearchNode('ㅇ')