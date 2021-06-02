from seoul.iris.IrisExcelFileReader import IrisExcelFileReader
from seoul.iris.IrisXmlFile import IrisXmlFile
from seoul.iris.IrisTableScript import IrisTableScript
#from seoul.iris.IrisCtlFile import IrisCtlFile
import sys
import yaml

excel_path = 'C:/Users/ff/PycharmProjects/psjLib/data/excel/6.자동차과태료시스템_short.xlsm'

conf = {}

with open('C:/Users/ff/PycharmProjects/psjLib/data/conf/conf.yml', encoding='UTF8') as cf:
    conf = yaml.load(cf, Loader=yaml.FullLoader)
    #print(conf)
    #print(type(conf['irisDataType']['TEXT']))
    #print(type(conf))

"""
irisExcel = IrisExcelFileReader(excel_path, header=0, usecols='A:Q', sheet_name='2. 대상컬럼')

wholeDict = irisExcel.getWholeDict(irisExcel.getTargetDf())

print(wholeDict)

irisXml = IrisXmlFile('C:/Users/ff/PycharmProjects/psjLib/data/xml/table_template_1.xml')
irisXml.generateXml(wholeDict['CARMAN.TB_ADSTRD'])
irisXml.writeToFile('C:/Users/ff/PycharmProjects/psjLib/data/output', 'CARMAN-TB_ADSTRD.xml')
"""

irisTable = IrisTableScript(conf['irisDataType'], conf['irisTableOption'])
irisTable.generateTableScript('C:/Users/ff/PycharmProjects/psjLib/data/output/CARMAN-TB_ADSTRD.xml')

#print(sys.path)

"""
f_df = df[(df['대상여부'].str.lower() == 'y') | (df['대상여부'].str.lower() == '?')].fillna("")

docXml = ET.parse("C:/Users/ff/PycharmProjects/psjLib/data/xml/table_template_1.xml")
rootEl = docXml.getroot()
cols = rootEl.find("cols")
selectQuery = []

for key, group in f_df.groupby(['OWNER', '테이블명']): # OWNER 와 테이블명 으로 중복되지 않게 그룹
    print(key)
    print(group.head(2))
    print(group.columns)

    is_init = True
    owner = key[0]
    tb_eng_name = key[1]
    #group.fillna("eee")

    for index in group.index:
        if is_init:
            rootEl.find("owner").text = owner
            rootEl.find("eng_name").text = key[1]
            rootEl.find("kor_name").text = group._get_value(index, '테이블 한글명')
            # rootEl.find("comment").text = "코멘트 내용"
        col = ET.SubElement(cols, "col")

        col_origin_eng_name = ET.SubElement(col, "origin_eng_name")
        col_origin_kor_name = ET.SubElement(col, "origin_kor_name")
        col_origin_data_type = ET.SubElement(col, "origin_data_type")

        origin_eng_name = group._get_value(index, '컬럼명')
        selectQuery.append(origin_eng_name)

        col_origin_eng_name.text = origin_eng_name
        col_origin_kor_name.text = group._get_value(index, '컬럼 한글명')
        col_origin_data_type.text = group._get_value(index, 'DATA_TYPE')

        col_convert_eng_name = ET.SubElement(col, "convert_eng_name")
        col_convert_kor_name = ET.SubElement(col, "convert_kor_name")
        col_convert_data_type = ET.SubElement(col, "convert_data_type")

        data_type = group._get_value(index, '데이터타입')

        col_convert_eng_name.text = group._get_value(index, '표준용어 영문명')
        col_convert_kor_name.text = group._get_value(index, '② 표준용어')
        col_convert_data_type.text = data_type

        cut_data_type = strUtil.cutStr(data_type, '(')



        #print(group._get_value(index, '컬럼명'))

    break


selectQueryEl = ET.Element('select_query')
selectQueryEl.text = ", ".join(selectQuery)

rootEl.insert(3, selectQueryEl)
xmlTest.apply_indent(rootEl)

docXml.write("C:/Users/ff/PycharmProjects/psjLib/data/output/table_template_1_out.xml",
    encoding="utf-8", xml_declaration=True)
    
for name, group in excel_df.groupby('테이블명'):
    print(name)
    print(group)

print(type(excel_df.groupby('테이블명')))
print(excel_df.groupby('테이블명').grouped)


print(excel_df.groupby('테이블명').groups)
print(excel_df.groupby('테이블명').size())
print(type(excel_df.groupby('테이블명').size()))
#print(excel_df.groupby('테이블명').get_group())
"""

"""
for index, row in excel_df.iterrows():
    print(type(index))
    print(index)
    print('~~~~~~')

    print(type(row))
    print(row)
    print('------')

    #print(row['point'])
    #print(row[2])
    #print(row.point)
    #print('======\n')
"""













"""
for excel_file_nm in uFile.getFilePathList("C:/Users/ff/PycharmProjects/psjLib/data/excel"):
    print(excel_file_nm.name)
"""