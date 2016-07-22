from src.Initialize import *;
from src.Room import RoomList

obj = Initialize(RoomList());

for room in obj.getRoomList():
    print('Room #' + str(room.getId()) + ':');
    print('    North: ' + str(room.goNorth().getId()) + ' - South: ' + str(room.goSouth().getId()));
    print('    West: ' + str(room.goWest().getId()) + ' - East: ' + str(room.goEast().getId()));
    print('    Danger: ' + room.getDanger());


startroom_N = obj.getRoomList().get(1);
startroom_E = obj.getRoomList().get(1);
startId = startroom_N.getId();
for i in range(0,NUMBER_OF_ROOMS+1):
    startroom_N = startroom_N.goNorth();
    startroom_E = startroom_E.goEast();
    if startId == startroom_N.getId() and startId == startroom_E.getId():
        if i == NUMBER_OF_ROOMS-1:
            print('Exiting trip. All is good');
        else:
            print('Exiting trip. Total of ', (i+1), ' steps');
        quit()
print('Error in room setup');