import json
import xml.etree.ElementTree as ET
from itertools import groupby

from conf.argpase_work import Argpase
from conf.open_file import OpenFile
from conf.students_conf import StudentsData


class HostelStudents:
    """ Load files  students.json, rooms.json, unite them into room's list, where room
     contains the list of students in this room, save JSON and XML. """

    def __init__(self, rooms, students):
        self.rooms = rooms
        self.students_list = students

        
    def check_room_unique(self):
        """ Check the repeating rooms, name their numbers """

        data_rooms = self.rooms
        list_rooms = list((d | {'students': []} for d in data_rooms))
        return  list_rooms

    def settle_students_room(self):
        # students = self.group_data_by_key()
        students = StudentsData(self.students_list).group_data_by_key()
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
