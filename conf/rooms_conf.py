class RoomsData:
    def __init__(self, rooms):
        self.rooms = rooms

    def check_room_unique(self):
        """ Check the repeating rooms, name their numbers """

        data_rooms = self.rooms
        list_rooms = list((d | {'students': []} for d in data_rooms))
        return list_rooms
