''' 
    @author Anton Möller
    File: Room.py, containing Room.class and RoomList.class
    2015, November 24th 
'''
from src import Static;
from src.Validate import getAssertDirection;

# Room.class is a room object defining a room by its ID, neighbours and a specified danger.
class Room():
    __north = None;
    __south = None;
    __west = None;
    __east = None;
    
    def __init__(self, mId, danger = Static.NONE):
        self.__mId = mId;
        self.__danger = danger;
    
    def setDanger(self, danger):
        assert (danger == Static.WUMPUS or danger == Static.NONE or danger == Static.BAT or danger == Static.HOLE),'Must be a valid danger'
        self.__danger = danger;
        
    def getDanger(self):
        return self.__danger;
    
    def getId(self):
        return self.__mId;
    
    # Returns the neighbour in the given direction
    def go(self, direction):
        if not getAssertDirection(direction) == None:
            if direction == Static.DIRECTION_NORTH:
                return self.__north;
            elif direction == Static.DIRECTION_SOUTH:
                return self.__south;
            elif direction == Static.DIRECTION_EAST:
                return self.__east;
            elif direction == Static.DIRECTION_WEST:
                return self.__west;
        else:
            #raise Exception('Requested direction is not valid');
            return None;
    
    def setNorth(self, room):
        assert isinstance(room, Room),'Must be of type Room.class'
        self.__north = room;
    def setSouth(self, room):
        assert isinstance(room, Room),'Must be of type Room.class'
        self.__south = room;
    def setEast(self, room):
        assert isinstance(room, Room),'Must be of type Room.class'
        self.__east = room;
    def setWest(self, room):
        assert isinstance(room, Room),'Must be of type Room.class'
        self.__west = room;
    
    def __str__(self):
        return str(self.mId) + ' ' + self.danger;
    
    # Returns the dangers of the surrounding rooms
    def getSurroundingDangers(self):
        return [self.__north.getDanger(), self.__south.getDanger(), self.__east.getDanger(), self.__west.getDanger()];
    
    # Returns the surrounding rooms themselves
    def getSurroundingRooms(self):
        return [self.__north.getId(), self.__south.getId(), self.__east.getId(), self.__west.getId()];
         
# RoomList.class holds a list of Room objects, built on a dictionary.
class RoomList():
    def __init__(self):
        self.__mList = {};
    
    def put(self,item):
        assert isinstance(item, Room), 'Can only put rooms into a roomlist!';
        self.__mList[str(item.getId())] = item;
        
    def get(self, ID):
        return self.__mList.get(str(ID), None);
    
    def isempty(self):
        return (self.__len__() == 0);    
    
    def __str__(self):
        return self.__mList.__str__();
    
    def __iter__(self):
        return iter(self.__mList.values());
    
    def __len__(self):
        return self.__mList.__len__();
    
