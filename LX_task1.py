import json
from itertools import groupby
import xml.etree.ElementTree as ET


class HostelStudents:
    """  """

    def __init__(self, rooms, students):
        self.rooms = rooms
        self.students = students

    def open_file(self, value):
        """ Загружаем данные из JSON"""

        with open(value, 'r', encoding='utf-8') as file:
            return json.load(file)

    def receive_key(self, item):
        """ Ф-я для получения элемента, который используется при группировке и сортировке в качестве ключа"""

        return item['room']  # №подумать (пересмотреть переменные)

    def sort_data_by_key(self):
        """ Сортирует данные по ключу """

        data_file = self.open_file(self.students)  # -------
        return sorted(data_file, key=self.receive_key)

    def group_data_by_key(self):
        """ Группирует данные по ключу """

        students_group = []
        sorted_data = self.sort_data_by_key()
        for key, group_items in groupby(sorted_data, key=self.receive_key):
            c = {key: [item for item in group_items]}
            students_group.append(c)
            # print('Комната: %s' % key)
            # ssss = []
            # for item in group_items:
            #     del item['room']
            #     # c= {key:[item for item in group_items ]}
            #     ssss.append(item)
            # students_group.append({key:ssss})
            # print('Студент: %s' % item)
        return students_group

    def check_room_unique(self):
        """ Проверет нет ли повторяющихся комнат, выводим их номера """

        data_rooms = self.open_file(self.rooms)
        list_rooms = (d.pop('name').replace('Room #', '') for d in data_rooms)
        list_rooms = set(list_rooms)
        number_room_int = [int(number) for number in list_rooms]
        # print(sorted(number_room_int))
        return number_room_int

    def delete_in_data_students_room(self, data_students):
        """ Удалил  """

        data_student = []
        for i in data_students:
            del i['room']
            data_student.append(i)
        return data_student

    def settle_students_room(self):
        count = 0
        data_for_save = []
        number_room = self.check_room_unique()
        students = self.group_data_by_key()
        for i in students:
            for key, value in i.items():
                if key in number_room:
                    value = self.delete_in_data_students_room(value)
                    data_for_save.append({
                        'id': count,
                        'room': f"Room #{key}",
                        'students': value
                    })
                    count = count + 1
        print(data_for_save)
        return data_for_save

    def generate_studens_room_for_save_XML(self):
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
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def saveXML(self):
        # data = self.settle_students_room()
        # root = ET.Element('root')
        # for group_stud in data:
        #     room = ET.SubElement(root, "room")
        #     ET.SubElement(room, 'id').text = str(group_stud['id'])
        #     ET.SubElement(room, 'name').text = str(group_stud['room'])
        #     student = ET.SubElement(room, 'student')
        #     for i, item in enumerate(group_stud['students'], 1):
        #         ET.SubElement(student, 'id').text = str(item['id'])
        #         ET.SubElement(student, 'name').text = item['name']

        tree = ET.ElementTree(self.generate_studens_room_for_save_XML())
        tree.write("details1.xml", encoding='utf-8')


a = HostelStudents('rooms.json', 'students.json')
# a.group_data_by_key()
a.save()
a.saveXML()
