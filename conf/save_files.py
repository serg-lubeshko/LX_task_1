import json
import xml.etree.ElementTree as ET


class SaveFiles:


    def save_xml(self, data_list):
        """ Generate data for saving in XML and save """

        data = data_list
        root = ET.Element('root')
        for group_stud in data:
            room = ET.SubElement(root, "room")
            ET.SubElement(room, 'id').text = str(group_stud['id'])
            ET.SubElement(room, 'name').text = str(group_stud['name'])
            student = ET.SubElement(room, 'student')
            for i, item in enumerate(group_stud['students'], 1):
                ET.SubElement(student, 'id').text = str(item['id'])
                ET.SubElement(student, 'name').text = item['name']

        tree = ET.ElementTree(root)
        tree.write("ResultXML.xml", encoding='utf-8')
        return tree

    def save_json(self, data_list):
        """ save json"""
        data = data_list
        with open('ResultJSON.json', 'w') as f:
            json.dump(data, f)
