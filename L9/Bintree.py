class Bintree():
    def __init__(self):
        self.__root = None;
        self.__printList = [];
        
    def put(self, item):
        if self.isempty():
            self.__root = TreeNode(item);
            return True;
        elif not self.exists(item):                
            root = self.__root;
            while True:
                if item > root.getValue():
                    if not root.getChildRight() == None:
                        root = root.getChildRight();
                    else:
                        root.setChildRight(TreeNode(item));
                        return True;
                elif item < root.getValue():
                    if not root.getChildLeft() == None:
                        root = root.getChildLeft();
                    else:
                        root.setChildLeft(TreeNode(item));
                        return True;
                else:
                    raise Exception('Unexpected error in put.');
        else:
            return False;
            
    def exists(self, item):
        if self.isempty():
            return False;
        
        root = self.__root;
        while True:
            if item == root.getValue():
                return True;
            elif item > root.getValue():
                if not root.getChildRight() == None:
                    root = root.getChildRight();
                else:
                    return False;
            elif item < root.getValue():
                if not root.getChildLeft() == None:
                    root = root.getChildLeft();
                else:
                    return False;
            else:
                raise Exception('Unexpected error in exists');
        
    def isempty(self):
        return self.__root == None;
    
    def height(self):
        return self.__heightRecursive(self.__root);
        
    def __heightRecursive(self, node):
        if node == None:
            return 0;
        else:
            return max(self.__heightRecursive(node.getChildLeft()), self.__heightRecursive(node.getChildRight())) + 1;

    def printtree(self):
        self.__printList = [];
        self.__printRecursive(self.__root);
        print(self.__printList);
    
    def getTree(self):
        self.__printList = [];
        self.__printRecursive(self.__root);
        return self.__printList;
        
    def __printRecursive(self, node):
        if node == None:
            return;
        
        if not node.getChildLeft() == None:
            self.__printRecursive(node.getChildLeft()); 
        self.__printList += [node.getValue()]; 
        if not node.getChildRight() == None:
            self.__printRecursive(node.getChildRight()); 
        
class TreeNode():
    def __init__(self, value, left = None, right = None):
        self.__left = left;
        self.__right = right;
        self.__value = value;
        
    def getValue(self):
        return self.__value;
    
    def getChildLeft(self):
        return self.__left;
    
    def getChildRight(self):
        return self.__right;
    
    def setChildLeft(self, left):
        self.__left = left;
        
    def setChildRight(self, right):
        self.__right = right;
    def __str__(self):
        if self.__value == None:
            return '';
        else:
            return self.__value;
    

