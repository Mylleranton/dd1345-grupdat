from Queue import Queue;
import time
class WordNode:
    def __init__(self, father = None, word = None):
        self.__father = father;
        self.__word = word.lower();
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
    def __hash__(self): 
        return self.getWord().__hash__();
    

wordList = open('word3u.txt', 'rt', encoding='utf8').read().split();
letters = 'abcdefghijklmnopqrstuvwxyzåäö';

wordSet = set();
for word in wordList:
    wordSet.add(word);

childrenGenerated = dict();


def generateChildren(wordNodeFather):
    objectSet = set()
    father = wordNodeFather.getWord();
    for i in range(0, len(father)): 
        for j in range(0, len(letters)):
            possibleWord = father[:i] + letters[j] + father[i+1:];
            if possibleWord in wordSet and not possibleWord == father:
                objectSet.add(WordNode(wordNodeFather, possibleWord));
    return objectSet;

def search(startWord):
    distance = 0;
    quene = Queue();
    seenKids = dict();
    
    father = WordNode(None, startWord);
        
    quene.put([father, distance]);
    seenKids[father] = distance;
    
    
    while not quene.isempty():
        word, dist = quene.get();
        
        if word in childrenGenerated:
            children = childrenGenerated[word];
        else:
            children = generateChildren(word);
            childrenGenerated[word] = children;
            
        for kid in children:
            if not kid in seenKids:
                seenKids[kid] = dist+1; 
                quene.put([kid, dist+1]);
            elif kid in seenKids and seenKids[kid] > dist+1:
                seenKids[kid] = dist+1;
                quene.put([kid, dist+1]);
    
    maxDepth = max(iter(seenKids.values()));
    for key, value in seenKids.items():
        if value == maxDepth:
            path = [];
            node = key;
            while not node.getFather() == None:
                path += [node.getWord()];
                node = node.getFather();
            path += [startWord];
            path.reverse();
#             print('Väg från ', startWord, 'till', key.getWord(), 'med', value, 'steg');
#             outstring = '';
#             for word in path:
#                 outstring += word + ' -> ';
#             print(outstring);
            return path, value; 
    
def longestDistance():
    longestPath = 0;
    results = [];
    for word in wordSet:
        path, value = search(word);
        if value > longestPath:
            results = [[path[0], path[-1]]];
            longestPath = value;
        elif value == longestPath:
            results += [[path[0], path[-1]]];
    print(longestPath);
    print(results);

t0 = time.time()
longestDistance();
t1 = time.time()
 
print('Time: ',t1-t0);
            
            
            
     
    
           
    
    
    

        