#coding: latin1

from queue_node import Queue
#from queue import Queue

mening = input("Skriv en mening: ")

myq = Queue()                 # skapa en tom kö

for ordet in mening.split():  # dela upp meningen i ord
    myq.put(ordet)            # och sätt in alla ord i kön

while not myq.isempty():      # alla köns element
    print(myq.get())          # skrivs ut

print()                       # tom rad
print(myq.get())              # None skrivs ut eftersom kön är tom