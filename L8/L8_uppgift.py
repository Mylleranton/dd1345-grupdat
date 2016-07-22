from Bintree import Bintree;
def uppgift2():
    # Problem vid ordnad lista. Blanda före insättning.
    wordList = open('15wordu.txt', 'rt', encoding='utf8').read().split();
    tree = Bintree();
    for word in wordList:
        tree.put(word);
    print('Trädets höjd är', tree.height());

def uppgift3():
    wordList = open('word3u.txt', 'rt', encoding='utf8').read().split();
    tree = Bintree();
    for word in wordList:
        if not tree.put(word):
            print(word);

def uppgift4():
    wordList = open('word3u.txt', 'rt', encoding='utf8').read().split();
    wordListEngInput = open('englishu.txt', 'rt', encoding='utf8').read().split();
    tree = Bintree();
    treeEng = Bintree();
    for word in wordList:
        tree.put(word);
    for word in wordListEngInput:
        word = word.strip('".!?, ').lower();
        if (tree.exists(word) and treeEng.put(word)):
            print(word);


        
        
            