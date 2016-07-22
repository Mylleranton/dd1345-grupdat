class Node():
    def __init__(self, v = None, n = None):
        self.item = v
        self.next = n
        
class Queue:
    def __init__(self):
        self.firstitem = None;
        self.lastitem = None;
    
    def put(self,item):
        node = Node(item,None);
        if self.isempty():
            self.firstitem = node;
        else:
            tmp_firstitem = self.firstitem;
            while not tmp_firstitem.next == None:
                tmp_firstitem = tmp_firstitem.next;
            tmp_firstitem.next = node; 
        self.lastitem = node;
        
    def get(self):
        if not self.isempty():
            item = self.firstitem.item;
            self.firstitem = self.firstitem.next;
            return item;
        else:
            return None;
    def isempty(self):
        return self.firstitem == None;
    
