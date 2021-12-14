class RoomsData:
    def __init__(self, rooms):
        self.rooms = rooms

    def get_room_new_list(self):


        data_rooms = self.rooms
        list_rooms = list((d | {'students': []} for d in data_rooms))
        return list_rooms
