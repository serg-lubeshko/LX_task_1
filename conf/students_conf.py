from itertools import groupby


class StudentsData:

    def __init__(self, students):
        self.students = students


    @staticmethod
    def receive_key(item):
        """ Get Key's element, which used for grouping and sorting"""
        """ Ф-я для получения элемента ключа, который используется при группировке и сортировке"""
        return item['room']

    def sort_data_by_key(self):
        """ Sort the data by Key """
        data_file = self.students
        print(data_file)
        return sorted(data_file, key=self.receive_key)

    def group_data_by_key(self):
        """ Group data by key; group students into rooms """
        students_group_room = {}
        sorted_students_room = self.sort_data_by_key()
        for room, group_students in groupby(sorted_students_room, key=self.receive_key):
            students_group_room[room]=[student for student in group_students]
        return students_group_room
