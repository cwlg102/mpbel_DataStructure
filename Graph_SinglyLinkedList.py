#Graph_SinglyLinkedList
class Node: #노드 클래스는 데이터 객체와 비어있는 다음값 객체로 주어짐
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, data='SinglyLinkedList'): #기준 머리를 잡아준다(불변)
        self.headnode = Node(data)

    def AddTail(self, data): #headnode에 불변의 노드가 들어가 있음 
        node = self.headnode
        while node.next != None: #None이 아닐때까지 하나씩 반복하면서 확인 #while node.next로 써도되나 개념공부를 위해
            node = node.next #node.next가 None이아니면 하나 넘김!
        #만약 None이면 튀어나와서
        node.next = Node(data) #해당 노드의 next레퍼에 추가할 노드를 연결해줌 
        ########근데 tail을 시작할때 정해놓으면 위와같은 while문을 돌필요가없을듯########

    #Node의 data변수엔 data를넣어주고 next 객체변수에 다음 Node클래스를 연결해주는것이 핵심
    #기본적으로 존재하는 더미 노드 뒤에다 넣어줌
    def AddHead(self, data): 
        newhead = Node(data)
        newhead.next = self.headnode.next
        self.headnode.next = newhead


    def InsertNode(self, prevdata, data):
        node = self.headnode
        while node.next != None: #순회
            if node.data == prevdata: #삽입할 위치의 이전 노드를 찾으면.
                ins_node = Node(data) #삽입 데이터의 노드를 ins_node로 생성.
                ins_node.next = node.next #삽입위치 이전 노드가 가리키던 next는, 삽입 데이터 노드의 next가 됨.
                node.next = ins_node #삽입위치 이전 노드가 가리키는 next는, 삽입 데이터 노드가 됨.
                break        
            node = node.next #못찾으면 다음 노드로 넘어감

    def DeleteNode(self, deldata):
        node = self.headnode #생성이 아니라 기존에 가지고있는걸 지우는 용도이기 때문에 InsertNode처럼 
        #temp = Node(data)이런식으로 생성하고 그거로 판단하면안됨
        if node.next.data == deldata:
            node.next = node.next.next
        while node.next != None:
            if node.next.data == deldata: #node.next자체가 Node(다음데이터)를 가리키는거라
                #node.next.data하면 다음노드에 있는 데이터임
                node.next = node.next.next
                break
            node = node.next
    
    def SearchNode(self, data):
        idx = -1
        node = self.headnode
        switch = 0
        while node.next != None:
            if node.data == data:
                print('Find!!!', node.data)
                print('Find!!!, Index:', idx) 
            node = node.next
            idx += 1
            switch = 1

        if node.data == data:
            print('Find!!!', node.data)
            print('Find!!!, Index:', idx)
            switch = 1

        if switch == 0:
            print('찾는값 없음')
    
    def ShowList(self): #리스트 보여주기용
        node = self.headnode
        while node.next != None:
            print(node.data, end=' ')
            node = node.next
        print(node.data)
    
    

class Graph:
    def __init__(self):
        self.vertex = [] #각 Linked List들을 관리할 list
    
    def addVer(self, v1, v2):
        v1flag = 0
        v2flag = 0
        
        for v in self.vertex: #이미 있는 값을 거르기 위한 과정
            if v.headnode.data == v1:
                v1flag = 1
            if v.headnode.data == v2:
                v2flag = 1
            
        
        if v1flag == 0 and v2flag == 0: #넣을 값이 둘다 존재하지않는다면 둘사이 간선을 만들기
            tmp1= SinglyLinkedList(v1) 
            tmp2= SinglyLinkedList(v2)
            tmp1.AddTail(v2)
            tmp2.AddTail(v1)
            self.vertex.append(tmp1)
            self.vertex.append(tmp2)

        elif v1flag == 1 and v2flag == 0: #v1 vertex가 존재할 경우
            for v in self.vertex:
                if v.headnode.data == v1:
                    tmp2 = SinglyLinkedList(v2)
                    tmp2.AddTail(v1)
                    v.AddTail(v2)
                    self.vertex.append(tmp2)
        elif v1flag == 0 and v2flag == 1: #v2 vertex가 존재할 경우
            for v in self.vertex:
                if v.headnode.data == v2:
                    tmp1 = SinglyLinkedList(v1)
                    tmp1.AddTail(v2)
                    v.AddTail(v1)
                    self.vertex.append(tmp1)
        #넣을값이 둘다 존재하나, 둘간의 edge가 없을때
        elif v1flag == 1 and v2flag == 1:
            for v in self.vertex:
                if v.headnode.data == v1:
                    node = v.headnode.next
                    while node.next:
                        if node.data == v2:
                            return
                        node = node.next
                    if node.data == v2:
                        return
                    else:
                        v.headnode.AddTail(v2) #node.next = Node(v2)이런식으로 해도됨
                if v.headnode.data == v2:
                    node = v.headnode.next
                    while node.next:
                        if node.data == v1:
                            return
                        node = node.next
                    if node.data == v1:
                        return
                    else:
                        v.headnode.AddTail(v1)
    def deleteVer(self, delver):
        for v in self.vertex:
            if v.headnode.data == delver:
                v.headnode = None #갯수변경 위험때문에 먼저 None으로 바꾸고
            else:
                v.DeleteNode(delver)
        for v in self.vertex:
            if v.headnode == None: #None이면 remove
                self.vertex.remove(v)

    def Visualization(self):
        for v in self.vertex:
            v.ShowList()
    
    def DFS(self, data, visited = []):
        for v in self.vertex: #self.vertex리스트를 하나씩 검사
            if len(visited) == len(self.vertex):
                return #재귀의 종료조건
            if v.headnode.data == data: #만약 검사를 시작할 data가 headnode라면
                visited.append(v.headnode.data) #방문한 것은 visited에 넣어줌
                print(v.headnode.data) #출력
                node = v.headnode.next #다음 노드부터 돌림
                while node.next: 
                    if node.data not in visited: #만약 LinkedList에 방문하지 않은 값이 있다면
                        self.DFS(node.data, visited) #DFS를 수행
                    node = node.next #그다음 노드로 넘어가기
                if node.data not in visited:
                    self.DFS(node.data, visited)
                        
            

a = Graph()
'''a.addVer(1, 2)
a.addVer(1, 5) #5있고
a.addVer(1, 7)
a.addVer(2, 3)
a.addVer(3, 4) #4 있으므로
a.addVer(4, 5) #여기서 연결을 진행을 안하게됨
a.addVer(4, 10)
a.addVer(5, 6)
a.addVer(6, 7)
a.addVer(6, 9)
a.addVer(7, 8)
a.addVer(8, 9)
a.addVer(9, 10)'''
a.addVer(1, 5)
a.addVer(1, 2)
a.addVer(2, 3)
a.addVer(3, 4)
a.addVer(5, 10)
a.addVer(10, 11)
a.addVer(5, 6)
a.addVer(6, 8)
a.deleteVer(6)
print()
a.Visualization()
print()
a.DFS(5)