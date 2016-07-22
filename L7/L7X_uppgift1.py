from queue_node import Queue
from random import randint
# Maximalt antal siffror i talen
n = 3;
# Antal tal 
m = 1000;

numberQueue = Queue();
sortingList = [];

for i in range(0,m):
    number = str(randint(0,10**(n)-1));
    while len(number) < n:
        number = '0' + number;
    
    numberQueue.put(number);

for i in range(0,10):
    sortingList += [Queue()];

###
for i in range(0,n):
    while not numberQueue.isempty():
        number = numberQueue.get();
        sortingList[int(number[n-1-i])].put(number);
        
    for item in sortingList:
        while not item.isempty():
            numberQueue.put(item.get());
            
while not numberQueue.isempty():
    print(numberQueue.get());
