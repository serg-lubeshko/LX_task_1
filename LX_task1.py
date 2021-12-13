import json
from itertools import groupby
import xml.etree.ElementTree as ET


class HostelStudents:
    """ Load files  students.json, rooms.json, unite them into room's list, where room
     contains the list of students in this room, save JSON and XML. """

    def __init__(self, rooms, students):
        self.rooms = rooms
        self.students = students

    @staticmethod
    def open_file(files):
        """ Load data from JSON"""
        with open(files, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def receive_key(item):
        """ Get Key's element, which used for grouping and sorting"""
        """ Ф-я для получения элемента ключа, который используется при группировке и сортировке"""
        return item['room']

    def sort_data_by_key(self):
        """ Sort the data by Key """
        data_file = self.open_file(self.students)
        return sorted(data_file, key=self.receive_key)

    # def group_data_by_key(self):
    #     """ Group data by key; group students into rooms """
    #     students_group_room = []
    #     sorted_students_room = self.sort_data_by_key()
    #     for room, group_students in groupby(sorted_students_room, key=self.receive_key):
    #         students_group_room.append({room: [student for student in group_students]})
    #     return students_group_room

    def group_data_by_key(self):
        """ Group data by key; group students into rooms """
        students_group_room = {}
        sorted_students_room = self.sort_data_by_key()
        for room, group_students in groupby(sorted_students_room, key=self.receive_key):
            students_group_room[room]=[student for student in group_students]
        # print(students_group_room)
        return students_group_room


        
    def check_room_unique(self):
        """ Check the repeating rooms, name their numbers """
        data_rooms = self.open_file(self.rooms)
        # print(data_rooms)
        list_rooms = (d | {'students': []} for d in data_rooms)
        a=list(list_rooms)
        # print(a)
        return  a

    def settle_students_room(self):
        students = self.group_data_by_key()
        rooms =  self.check_room_unique()

        result =[]
        for room in rooms:
            # b=students[room['id']]
            room['students'].extend(students[room['id']])
            result.append(room)
        return result
    # def check_room_unique(self):
    #     """ Check the repeating rooms, name their numbers """
    #     data_rooms = self.open_file(self.rooms)
    #     list_rooms = (d.pop('name').replace('Room #', '') for d in data_rooms)
    #     list_rooms = set(list_rooms)
    #     number_room_int = [int(number) for number in list_rooms]
    #     return number_room_int




    # @staticmethod
    # def delete_in_data_students_room(data_students):
    #     """ Clean Key-meaning "room" in students' data """
    #     info_students = []
    #     for info_student in data_students:
    #         del info_student['room']
    #         info_students.append(info_student)
    #     return info_students

    # def settle_students_room(self):
    #     """ Unite rooms and students """
    #     count = 0
    #     data_for_save = []
    #     number_room = self.check_room_unique()
    #     students = self.group_data_by_key()
    #     for students_in_room in students:
    #         for room, students_info in students_in_room.items():
    #             if room in number_room:
    #                 students_in_room = self.delete_in_data_students_room(students_info)
    #                 data_for_save.append({
    #                     'id': count,
    #                     'room': f"Room #{room}",
    #                     'students': students_in_room
    #                 })
    #                 count = count + 1
    #     return data_for_save

    @property
    def generate_studens_room_for_save_xml(self):
        """ Generate data for saving in XML """
        data = self.settle_students_room()
        root = ET.Element('root')
        for group_stud in data:
            room = ET.SubElement(root, "room")
            ET.SubElement(room, 'id').text = str(group_stud['id'])
            ET.SubElement(room, 'name').text = str(group_stud['room'])
            student = ET.SubElement(room, 'student')
            for i, item in enumerate(group_stud['students'], 1):
                ET.SubElement(student, 'id').text = str(item['id'])
                ET.SubElement(student, 'name').text = item['name']
        return root

    def save(self):
        data = self.settle_students_room()
        with open('ResultJSON.json', 'w') as f:
            json.dump(data, f)

    def save_xml(self):
        tree = ET.ElementTree(self.generate_studens_room_for_save_xml)
        tree.write("ResultXML.xml", encoding='utf-8')


def main():
    result = HostelStudents('rooms.json', 'students.json')
    result.save()
    # result.save_xml
    result.settle_students_room()


if __name__ == '__main__':
    main()
