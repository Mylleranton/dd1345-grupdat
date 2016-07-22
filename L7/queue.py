class Queue:
    mList = [];
    def put(self,item):
        self.mList.append(item);
    def get(self):
        if not self.isempty():
            return self.mList.pop(0);
        else:
            return None;
    def isempty(self):
        return (len(self.mList) == 0);