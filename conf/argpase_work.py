import argparse


class Argpase():

    @staticmethod
    def work_argparse():
        # python main.py -h

        parser = argparse.ArgumentParser()

        # Позиционные
        parser.add_argument('r_students', type=str, nargs='?', const="students.json",
                            help='Route to students.json file', default="students.json")
        parser.add_argument('r_rooms', type=str, nargs='?', const="rooms.json", help='Route to rooms.json file',
                            default="rooms.json")
        args = parser.parse_args()
        print(args.r_students)
        print(args.r_rooms)
        
        return args
