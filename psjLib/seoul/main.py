import yaml
import glob

from lib.iris.IrisExcelFileReader import IrisExcelFileReader
from lib.iris.IrisXmlFile import IrisXmlFile
from lib.iris.IrisTableScript import IrisTableScript
from lib.iris.IrisCtlFile import IrisCtlFile

# conf.yml 파일 읽기
with open('../data/conf/conf.yml', encoding='UTF8') as cf:
    conf = yaml.load(cf, Loader=yaml.FullLoader)

# 테이블 정보 엑셀파일 이름 가져오기
file_list = glob.glob(conf['irisFilePaths']['tableExcelPath'] + '/*')

irisXml = IrisXmlFile(conf['irisFilePaths']['xmlTemplatePath'] + '/table_template_1.xml')
irisCtl = IrisCtlFile(conf['irisDataType'], conf['irisLoadFuncNm'])
irisTable = IrisTableScript(conf['irisDataType'], conf['irisTableOption'])

for excel_path in [file for file in file_list if file.endswith(".xlsm")]:
    # 테이블 정보 엑셀파일 읽기
    irisExcel = IrisExcelFileReader(excel_path, header=0, usecols='A:T', sheet_name='2. 컬럼목록', conf_dict=conf)
    wholeDict = irisExcel.getWholeDict(irisExcel.getTargetDf())

    # 엑셀파일의 테이블 정보 xml 파일로 만들기
    for key, tableDict in wholeDict.items():
        print('테이블명 : {} 정보 xml 파일 생성'.format(key))

        irisXml.generateXml(tableDict)
        irisXml.writeToFile(conf['irisFilePaths']['outputPath'] + '/table_xml', key + '.xml')

        irisCtl.generateCtlFile(key, tableDict['cols'], conf['irisFilePaths']['outputPath'] + '/table_ctl')

        irisTable.generateTableScript(conf['irisFilePaths']['outputPath'] + '/table_xml/' + key + '.xml',
                                      conf['irisFilePaths']['outputPath'] + '/table_script')
        break
