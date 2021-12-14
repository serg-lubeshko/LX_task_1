from conf.argpase_work import Argpase
from conf.open_file import OpenFile
from conf.rooms_conf import RoomsData
from conf.save_files import SaveFiles
from conf.students_conf import StudentsData


class HostelStudents:

    def __init__(self, rooms, students):
        self.rooms_list = rooms
        self.students_list = students
        self.save=SaveFiles()

    def settle_students_room(self):
        students = StudentsData(self.students_list).group_data_by_key()
        rooms =  RoomsData(self.rooms_list).get_room_new_list()
        result =[]
        for room in rooms:
            room['students'].extend(students[room['id']])
            result.append(room)
        return result





def main():
    arg_parser = Argpase.work_argparse()

    students_file=OpenFile.open_file(arg_parser.r_students)
    rooms_file = OpenFile.open_file(arg_parser.r_rooms)

    result = HostelStudents(rooms_file, students_file)

    data_save=result.settle_students_room()

    result.save.save_json(data_save)
    result.save.save_xml(data_save)



if __name__ == '__main__':
    main()
