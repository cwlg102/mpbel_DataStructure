#Stack_List
class Stack:
    def __init__(self, totalsize=10):
        self.stacklist = []
        self.totalsize = totalsize
        self.size = -1
    
    def PushData(self, data):
        if self.size == self.totalsize - 1:
            print('Nope')
        else:
            self.stacklist.append(data)
            self.size += 1
    
    def PopData(self):
        self.stacklist.pop(self.size)
        self.size -= 1
    
    def Top(self):
        print(self.stacklist[self.size])
    
    def EmptyCheck(self):
        if self.size == 0:
            print('Empty Stack')
        else:
            print(self.size)
    
    def PopAll(self):
        while self.size != -1:
            self.stacklist.pop(self.size)
            self.size -= 1

p = Stack()
for i in range(1, 10, 2):
    p.PushData(i)
p.PushData(4)
p.PushData(5)
p.PushData(41)
p.PushData(32)
p.PushData(3939)
p.PushData(33)
print(p.stacklist)
p.PopData()
print(p.stacklist)
p.Top()
p.PopAll()
print(p.stacklist)