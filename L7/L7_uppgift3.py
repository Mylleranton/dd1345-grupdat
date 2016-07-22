from queue_node import Queue;

class WordPair():
    def __init__(self, string = '', translation = '', iterations = 0):
        self.string = string;
        self.translation = translation;
        self.iterations = iterations;
    
    def getString(self):
        return self.string;
    def getTranslation(self):
        return self.translation;
    def getIterations(self):
        return self.iterations;
    def setIterations(self, iterations):
        self.iterations = iterations;

words = open('hawaiianu_test.txt', 'rt', encoding='utf8').read().split();
queue = Queue(); 
for i in range(0,int(len(words)/2)):
    k = 2*i;
    wordpair = WordPair(words[k],words[k+1]);
    queue.put(wordpair);


while not queue.isempty():
    word = queue.get();
    if word.getIterations() < 2:
        usrinput = input("Vad betyder: " + "'" + word.getString() + "'?");
        if usrinput == word.getTranslation():
            print('Rätt!')
            word.setIterations(word.getIterations() + 1);
            queue.put(word);
        else:
            print("Fel, rätt svar är: '" + word.getTranslation() +"'");
            queue.put(word);

print('Slut på glosförhöret!');
    
    

        




        
    
    
    

