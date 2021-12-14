import argparse
import os


class Argpase():

    @staticmethod
    def work_argparse():

        parser = argparse.ArgumentParser()

        parser.add_argument('r_students', type=str, nargs='?',
                            help='Route to students.json file', default="students.json")
        parser.add_argument('r_rooms', type=str, nargs='?', help='Route to rooms.json file',
                            default="rooms.json")
        args = parser.parse_args()

        print(args.r_students)
        print(args.r_rooms)

        return args
