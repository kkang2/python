import xml.etree.ElementTree as ET
from lib.iris.util.strUtil import cutStr

class IrisTableScript:
    def __init__(self, data_type_info, table_option_list):
        self.data_type_info = data_type_info
        self.table_option_list = table_option_list
        #print(table_option_list)

    def generateTableScript(self, tableXmlPath, tableScriptPath):
        tableScriptText = 'CREATE TABLE '
        rootEl = ET.parse(tableXmlPath).getroot()
        col_contents = []

        table_nm = rootEl.find('owner').text + '.' + rootEl.find('eng_name').text

        tableScriptText += table_nm + ' (\n'

        for col_el in rootEl.find('cols').findall('col'):
            origin_data_type = col_el.findtext('convert_data_type')
            cut_data_type = cutStr(col_el.findtext('convert_data_type').lower(), '(')
            col_nm = col_el.findtext('convert_eng_name')

            if cut_data_type in self.data_type_info['TEXT']:
                col_contents.append('\t' + col_nm + ' TEXT')
            elif cut_data_type in self.data_type_info['NUMBER']:
                if origin_data_type.find(',') < 0:
                    col_contents.append('\t' + col_nm + ' INTEGER')
                else:
                    col_contents.append('\t' + col_nm + ' REAL')
            else:
                col_contents.append('\t' + 'column type not found!')

        tableScriptText += ',\n'.join(col_contents) + ')\n' + '  값 셋팅 필요\n'.join(self.table_option_list) + '  값 셋팅 필요;'

        #print('최종 스크립트 문 : {}'.format(tableScriptText))

        with open(tableScriptPath + '/' + table_nm + '_script', "w", encoding='utf-8') as file:
            file.writelines(tableScriptText)


    def writeToFile(self, tableScriptPath, fileNm):
        self.docXml.write(tableScriptPath + '/' + fileNm, encoding="utf-8", xml_declaration=True)