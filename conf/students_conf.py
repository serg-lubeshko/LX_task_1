from itertools import groupby


class StudentsData:

    def __init__(self, students):
        self.students = students


    @staticmethod
    def group(item):
        """ Get Key's element, which used for grouping and sorting"""
        return item['room']


    def group_data_by_key(self):
        """ Group data by key; group students into rooms """

        students_group_room = {}
        data_students = sorted(self.students, key=self.group)
        for room, group_students in groupby(data_students, key=self.group):
            students_group_room[room]=[student for student in group_students]
        return students_group_room
