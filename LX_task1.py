import json
from itertools import groupby
import xml.etree.ElementTree as ET

from argpase_work import Argpase
from open_file import OpenFile


class HostelStudents:
    """ Load files  students.json, rooms.json, unite them into room's list, where room
     contains the list of students in this room, save JSON and XML. """

    def __init__(self, rooms, students):
        self.rooms = rooms
        self.students = students



    @staticmethod
    def receive_key(item):
        """ Get Key's element, which used for grouping and sorting"""
        """ Ф-я для получения элемента ключа, который используется при группировке и сортировке"""
        return item['room']

    def sort_data_by_key(self):
        """ Sort the data by Key """
        data_file = self.students
        return sorted(data_file, key=self.receive_key)

    def group_data_by_key(self):
        """ Group data by key; group students into rooms """
        students_group_room = {}
        sorted_students_room = self.sort_data_by_key()
        for room, group_students in groupby(sorted_students_room, key=self.receive_key):
            students_group_room[room]=[student for student in group_students]
        return students_group_room


        
    def check_room_unique(self):
        """ Check the repeating rooms, name their numbers """

        data_rooms = self.rooms
        list_rooms = list((d | {'students': []} for d in data_rooms))
        return  list_rooms

    def settle_students_room(self):
        students = self.group_data_by_key()
        rooms =  self.check_room_unique()

        result =[]
        for room in rooms:
            room['students'].extend(students[room['id']])
            result.append(room)
        return result

    @property
    def generate_studens_room_for_save_xml(self):
        """ Generate data for saving in XML """
        data = self.settle_students_room()
        root = ET.Element('root')
        for group_stud in data:
            room = ET.SubElement(root, "room")
            ET.SubElement(room, 'id').text = str(group_stud['id'])
            ET.SubElement(room, 'name').text = str(group_stud['name'])
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
    arg_parser = Argpase.work_argparse()
    students_file=OpenFile.open_file_json(arg_parser.r_students)
    rooms_file = OpenFile.open_file_json(arg_parser.r_rooms)


    result = HostelStudents(rooms_file, students_file)
    result.save()
    result.save_xml()
    
    # result.settle_students_room()


if __name__ == '__main__':
    main()
