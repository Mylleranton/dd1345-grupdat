class Bintree():
    def __init__(self):
        self.__root = None;
        self.__printList = [];
    def getRoot(self):
        return self.__root;
        
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
        
    def __printRecursive(self, node):
        if node == None:
            return;
        
        if not node.getChildLeft() == None:
            self.__printRecursive(node.getChildLeft()); 
        self.__printList += [node.getValue()]; 
        if not node.getChildRight() == None:
            self.__printRecursive(node.getChildRight()); 
            
    def remove(self, item):
        self.__removeFromRoot(item, self.__root);
        
    def __removeFromRoot(self, item, theroot):
        def __findMax(root):
            while not root.getChildRight() == None:
                root = root.getChildRight();
            return root;
        
        def __findMin(root):
            while not root.getChildLeft() == None:
                root = root.getChildLeft();
            return root;
        
        def __replaceInParent(parent, node, newNode = None):
            if node == self.__root:
                self.__root = newNode;
            elif not parent == None:
                if parent.getChildRight() == node:
                    parent.setChildRight(newNode);
                elif parent.getChildLeft() == node:
                    parent.setChildLeft(newNode); 
                else:
                    raise Exception('Error: parent', str(parent), 'has no child', str(node));
            else:
                raise Exception('IllegalArgument: parent cannot be none');
        
        parent, node = self.__findparent(item, theroot);
        
        if node == None:
            #raise Exception('IllegalArgument: node cannot be None');
            print(item, 'does not exist in the tree.');
            return False;
        
        # Has two children
        if not (node.getChildLeft() == None) and not (node.getChildRight() == None): 
            
            if self.__heightRecursive(node.getChildLeft()) > self.__heightRecursive(node.getChildRight()):
                # Use Left tree as successor
                newValue = __findMax(node.getChildLeft()).getValue();
                self.__removeFromRoot(newValue, node.getChildLeft());
                node.setValue(newValue);
                del newValue;
                return True;
            else:
                # Use Right tree as successor
                newValue = __findMin(node.getChildRight()).getValue();
                self.__removeFromRoot(newValue, node.getChildRight());
                node.setValue(newValue);
                del newValue;
                return True;
            
        # One child
        elif not node.getChildLeft() == None:
            __replaceInParent(parent, node, node.getChildLeft());
            return True;
        elif not node.getChildRight() == None:
            __replaceInParent(parent, node, node.getChildRight());
            return True;
        # No children
        else:
            __replaceInParent(parent, node, None);
            return True;
    
    def __findparent(self, value, aroot):
        if not self.exists(value):
            #raise Exception('IllegalArgument: ', value, ' is not in the tree.');
            return [None, None];
            
        if value == aroot.getValue():
            if not aroot == self.__root:
                parent, garbage = self.__findparent(value, self.__root);
                return [parent, aroot];
            return [None, aroot];
        
        parent = None;
        child = aroot;
        while True:
            if value == child.getValue():
                return [parent, child];
            elif value > child.getValue() and not child.getChildRight() == None:
                parent = child;
                child = child.getChildRight();
                continue;
            elif value < child.getValue() and not child.getChildLeft() == None:
                parent = child;
                child = child.getChildLeft();
                continue;
            else:
                raise Exception('Unexpected error in findparent');
    
              
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
        assert isinstance(left, TreeNode) or left == None, 'Must be istance of TreeNode or None';
        self.__left = left;
        
    def setChildRight(self, right):
        assert isinstance(right, TreeNode) or right == None, 'Must be istance of TreeNode or None';
        self.__right = right;
    
    def setValue(self, value):
        self.__value = value;
        
    def __str__(self):
        if self.__value == None:
            return 'Node: None';
        else:
            return 'Node:' + str(self.__value);
    

