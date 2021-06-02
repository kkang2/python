from lib.util.log import getLogger


print('1' + '%05d' % 44)




uu = 'dd'.split(':')

#print(uu[1])

#print("ooooo"[:1])

"""
str = '"{}":"{}"'.format('phone_number0', 'str')
#str = '\\{"phone_number0":"str"\\}'.format('phone_number0', 'str')
dict = str

print(dict)


dict = {'nn':{'tt':9}}

print(dict.get('nn').get('tt'))
print(dict.get('nn.tt'))


logger = getLogger('con_file_logger')

logger.info("인포메세지")

text = "replace(_col_, '어쩌고저쩌고구문')"

#print(eval("''.replace(_col_, '어쩌고저쩌고구문')"))

#print(text.replace('_col_', 'dsfdsfs'))
"""
"""
[IrisXmlFile_test]

import xml.etree.ElementTree as ET

docXml = ET.parse("C:/Users/ff/PycharmProjects/psjLib/data/xml/table_template_1.xml")

print(docXml)
print(docXml.getroot())

ET.dump(docXml.getroot())

docXml.getroot().remove(docXml.getroot().find('cols'))

ET.dump(docXml.getroot())

ET.SubElement(docXml.getroot(), 'cols')

ET.dump(docXml.getroot())

#docXml.write("C:/Users/ff/PycharmProjects/psjLib/data/output/table_template_2_out.xml",
#    encoding="utf-8", xml_declaration=True)

"""

"""
[IrisExcelFileReader_test

import pandas as pd

data = [
    ['1000', 'Steve', 90.72],
    ['1001', 'James', 78.09],
    ['1002', 'Doyeon', 98.43],
    ['1003', 'Jane', 64.19],
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14]
]

df = pd.DataFrame(data, columns=['학번', '이름', '점수'])

#df1 = df.reindex([1, 3, 4, 5, 0, 2])
df1 = df.reindex(columns=['이름', '점수', '학번'])

print(df)
print(df1)
print('전체로우 갯수 : {}'.format(len(df1)))

print(df.iloc[0]['학번'])
print(type(df.iloc[0]))

col = {'col':{'origin_eng_name'}}
col['col'] = {'owner':'CARMAN'}


print(col)

excel = rd.read_excel("C:/Users/ff/PycharmProjects/psjLib/data/excel/3.보도포장관리_시스템.xlsm", 0,
                   "A:Q", "1. 대상테이블")
print(excel.head(3))

data = [
    ['1000', 'Steve', 90.72],
    ['1001', 'James', 78.09],
    ['1002', 'Doyeon', 98.43],
    ['1003', 'Jane', 64.19],
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]
df = pd.DataFrame(data, columns=['학번', '이름', '점수'])
print(df)

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)
print(df)

print(df.index) # 인덱스 출력
print(df.columns) # 열 출력
print(df.values) # 값 출력

sr = pd.Series([17000, 18000, 1000, 5000], index=["피자", "치킨", "콜라", "맥주"])

print(sr)
print(sr.values)
print(sr.index)

"""
"""
[IrisCtlFile_test]

from IrisCtlFile import IrisCtlFile
import yaml

with open('C:/Users/ff/PycharmProjects/psjLib/data/conf/log_conf.yml', encoding='UTF8') as cf:
    conf = yaml.load(cf, Loader=yaml.FullLoader)

print(conf)

ctlFile = IrisCtlFile(conf['irisDataType'], conf['irisLoadFuncNm'])

ctlFile.generateCtlFile('TB_ADSTRD', {'ADSTRD_CD':'VARCHAR(10)', 'ADSTRD_NUM':'NUMBER(11)'}, 'C:/Users/ff/PycharmProjects/psjLib/data/output')

    from util.strUtil import *

data_type_info = {'TEXT': ['char', 'varchar', 'varchar2', 'nvarchar2'], 'NUMBER': ['number']}
col_info = {'ADSTRD_CD':'VARCHAR(10)', 'ADSTRD_NUM':'NUMBER(11)'}
col_convert_func_info = {'TEXT': 'to_text(?, null)', 'INT': 'to_int(?, null, 0)', 'REAL': 'to_real(?, null, 0.0)'}

ctl_contents = []

for key, value in col_info.items():
    value_type = cutStr(value.lower(), '(')

    print("key : {}, value_type : {}".format(key, value_type))

    if value_type in data_type_info['TEXT']:
        ctl_contents.append(key + ',' + col_convert_func_info['TEXT'])
    elif value_type in data_type_info['NUMBER']:
        if value.find(',') < 0:
            ctl_contents.append(key + ',' + col_convert_func_info['INT'])
        else:
            ctl_contents.append(key + ',' + col_convert_func_info['REAL'])

print(ctl_contents)
print(len(ctl_contents))
print(len([]))

    elif True:
        pass
    else:
        pass
"""