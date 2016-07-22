class QueueNode():
    def __init__(self, v = None, n = None):
        self.item = v
        self.next = n
        
class Queue:
    def __init__(self):
        self.__firstitem = None;
        self.__lastitem = None;
    
    def put(self, item):
        node = QueueNode(item,None);
        if self.isempty():
            self.__firstitem = node;
        else:
            tmp_firstitem = self.__firstitem;
            while not tmp_firstitem.next == None:
                tmp_firstitem = tmp_firstitem.next;
            tmp_firstitem.next = node; 
        self.__lastitem = node;
        
    def get(self):
        if not self.isempty():
            item = self.__firstitem.item;
            self.__firstitem = self.__firstitem.next;
            return item;
        else:
            return None;
    def isempty(self):
        return self.__firstitem == None;
    
