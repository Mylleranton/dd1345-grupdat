from src.main_backend import *;
from src.Static import *;

obj = None;
try:
    for i in range(0,100):
        obj = main_backend();
except:
    print('Error in assertion');
    quit();
    
print('\n\n\nAll is good!');

obj.move(DIRECTION_NORTH);
obj.move(DIRECTION_SOUTH);
obj.move(DIRECTION_EAST);
obj.move(DIRECTION_WEST);