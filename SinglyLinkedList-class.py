########################Singly Linked List########################
class Node: #노드 클래스는 데이터 객체와 비어있는 다음값 객체로 주어짐
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, data):
        self.headdummyNode = Node(data)

    def AddTail(self, data): #headdummyNode에 헤드노드가 들어감! 
        node = self.headdummyNode
        while node.next != None: #None이 아닐때까지 하나씩 반복하면서 확인 #while node.next로 써도되나 개념공부를 위해
            node = node.next #node.next가 None이아니면 하나 넘김!
        #만약 None이면 튀어나와서
        node.next = Node(data) #해당 노드의 next레퍼에 추가할 노드를 연결해줌 
        ########근데 tail을 시작할때 정해놓으면 위와같은 while문을 돌필요가없을듯########

    #Node의 data변수엔 data를넣어주고 next 객체변수에 다음 Node클래스를 연결해주는것이 핵심
    def AddHead(self, data): #무조건 이전 노드보다 앞에다 넣어줘야함
        newhead = Node(data)
        newhead.next = self.headdummyNode.next
        self.headdummyNode.next = newhead


    def InsertNode(self, prevdata, data):
        node = self.headdummyNode
        while node.next != None: #순회
            if node.data == prevdata: #삽입할 위치의 이전 노드를 찾으면.
                temp = Node(data) #삽입 데이터의 노드를 temp로 생성.
                temp.next = node.next #삽입위치 이전 노드가 가리키던 next는, 삽입 데이터 노드의 next가 됨.
                node.next = temp #삽입위치 이전 노드가 가리키는 next는, 삽입 데이터 노드가 됨.
                break        
            node = node.next #못찾으면 다음 노드로 넘어감

    def DeleteNode(self, deldata):
        node = self.headdummyNode #생성이 아니라 기존에 가지고있는걸 지우는 용도이기 때문에 InsertNode처럼 
        #temp = Node(data)이런식으로 생성하고 그거로 판단하면안됨
        while node.next != None:
            if node.next.data == deldata: #node.next자체가 Node(다음데이터)를 가리키는거라
                #node.next.data하면 다음노드에 있는 데이터임
                node.next = node.next.next
            node = node.next

p=SinglyLinkedList('시작점')
p.AddTail(5)
p.AddTail(6)
p.AddTail(2312)
p.AddTail(1212)
p.InsertNode(5, 100)
p.AddHead(33)
p.AddHead(51)
p.DeleteNode(6)
#출력 시험
node = p.headdummyNode
while node.next != None:
    print(node.data)
    node = node.next
print(node.data)



