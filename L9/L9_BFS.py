from Bintree import Bintree;
from Queue import Queue;
class WordNode:
    def __init__(self, father = None, word = None):
        self.__father = father;
        self.__word = word;
    def getWord(self):
        return self.__word;
    def getFather(self):
        return self.__father;

    def __lt__(self, other):
        if not isinstance(other, WordNode): return False;
        return self.getWord() < other.getWord();
    def __gt__(self, other):
        if not isinstance(other, WordNode): return False;
        return self.getWord() > other.getWord();
    def __eq__(self, other):
        if not isinstance(other, WordNode): return False;
        return self.getWord() == other.getWord(); 
    

wordList = open('word3u.txt', 'rt', encoding='utf8').read().split();
letters = 'abcdefghijklmnopqrstuvwxyzåäö';

wordTree = Bintree();
for word in wordList:
    wordTree.put(word);

def generateChildren(wordNodeFather):
    tree = Bintree()
    father = wordNodeFather.getWord();
    for i in range(0, len(father)): #for every letter in father
        for j in range(0, len(letters)):
            possibleWord = father[:i] + letters[j] + father[i+1:];
            if wordTree.exists(possibleWord) and not possibleWord == father:
                tree.put(WordNode(wordNodeFather, possibleWord));
    return tree.getTree();

def search(startWord, endWord):
    quene = Queue();
    tree = Bintree();
    father = WordNode(None, startWord);
    child = WordNode();
    
    quene.put(father);
    tree.put(father);
    
    while not quene.isempty():
        word = quene.get();
        if word.getWord() == endWord:
            child = word;
            break;
        else:
            children = generateChildren(word);
            for kid in children: 
                if tree.put(kid):
                    quene.put(kid);
                    
    if not child.getWord() == None:
        path = [];
        while not child.getFather() == None:
            path += [child.getWord()];
            child = child.getFather();
        path += [father.getWord()];
        
        path.reverse();
        print('Väg mellan', startWord, 'och', endWord);
        for item in path:
            print(item + ' -> ');
    else:
        raise Exception('No path found');
    
search('fan', 'gud');
     
    
           
    
    
    

        