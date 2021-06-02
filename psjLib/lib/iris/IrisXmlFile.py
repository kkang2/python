import xml.etree.ElementTree as ET

class IrisXmlFile:
    def __init__(self, templatePath):
        self.docXml = ET.parse(templatePath)
        self.rootEl = self.docXml.getroot()

    def generateXml(self, table_dict):
        col_nm_list = []
        self.__init_xml_el(self.rootEl)

        self.rootEl.find('owner').text = table_dict['owner']
        self.rootEl.find('eng_name').text = table_dict['eng_name']
        self.rootEl.find('kor_name').text = table_dict['kor_name']
        self.rootEl.find('comment').text = table_dict['comment']

        for col_dict in table_dict['cols']:
            cols_el = self.rootEl.find('cols')
            col_el = ET.SubElement(cols_el, 'col')
            origin_eng_name = col_dict['col']['origin_eng_name']

            if col_dict.get('col').get('select_origin_eng_name') != None:
                col_nm_list.append(col_dict['col']['select_origin_eng_name'])
            else:
                col_nm_list.append(origin_eng_name)

            ET.SubElement(col_el, "origin_eng_name").text = origin_eng_name
            ET.SubElement(col_el, "origin_kor_name").text = col_dict['col']['origin_kor_name']
            ET.SubElement(col_el, "origin_data_type").text = col_dict['col']['origin_data_type']
            ET.SubElement(col_el, "convert_eng_name").text = col_dict['col']['convert_eng_name']
            ET.SubElement(col_el, "convert_kor_name").text = col_dict['col']['convert_kor_name']
            ET.SubElement(col_el, "convert_data_type").text = col_dict['col']['convert_data_type']

        self.rootEl.find('select_query').text = ', '.join(col_nm_list)
        self.apply_indent(self.rootEl)
        #ET.dump(self.rootEl)

    def writeToFile(self, xmlFolderPath, fileNm):
        self.docXml.write(xmlFolderPath + '/' + fileNm, encoding="utf-8", xml_declaration=True)

    def __init_xml_el(self, rootEl):
        rootEl.find('owner').text = ''
        rootEl.find('eng_name').text = ''
        rootEl.find('kor_name').text = ''
        rootEl.find('select_query').text = ''
        rootEl.find('comment').text = ''
        rootEl.remove(rootEl.find('cols'))
        ET.SubElement(rootEl, 'cols')

    def apply_indent(self, elem, level=0):
        # tab = space * 2
        indent = "\n" + level * "    "

        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = indent + "    "
            if not elem.tail or not elem.tail.strip():
                elem.tail = indent
            for elem in elem:
                self.apply_indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = indent
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = indent