import xml.etree.ElementTree as ET
import pandas as pd

from lib.util.date import Date
from lib.iris.util.partition_key_util import *
from lib.iris.util.partition_date_util import *
from lib.file.fileUtil import *

class CsvSplitter:
    def __init__(self, basic_file_path, csv_file_nm, table_info_xml_nm):
        self.basic_file_path = basic_file_path
        self.csv_file_nm = csv_file_nm
        self.table_info_doc = ET.parse(basic_file_path + '/' + table_info_xml_nm)

    def splitCsv(self):
        #dtype = eval("{'FDL_9':'str'}") # 추후에 추가할것
        dtype = eval("{}")

        # 20210601,extract_numType1:FDL_I1,extract_fixDate1
        split_rule = self.table_info_doc.getroot().find('csv_split_rule').text.split(',')

        print(split_rule)
        
        df = pd.read_csv(self.basic_file_path + '/' + self.csv_file_nm, encoding='utf-8', header=0, sep='', dtype=dtype)  # 숫자 앞에 0 짤리는걸 방지하기 위해 dtype값을 줌

        # 파티션 키/데이터 값 넣기

        self.insertIrisColumn(df, split_rule)
        #self.insertPartitionKey(df, split_rule[0])
        #self.insertPartitionDate(df, split_rule[1])

        #print(df)

        for key, group in df.groupby('partition_key'):
            print("key :{}".format(key))

            rowSeries = group.head(1).get('partition_date')
            save_folder = self.basic_file_path + '/split_data/' + Date.curDateStr('%Y%m%d')

            print('whole file path : {}/{}_{}'.format(save_folder, key, rowSeries[rowSeries.index[0]]))

            createFolder(save_folder)

            group.to_csv(save_folder + '/{}_{}'.format(key, rowSeries[rowSeries.index[0]]), sep='', header=True,
                         index=False)

    def insertIrisColumn(self, df, split_rule):
        key_rule = split_rule[0]
        date_rule = split_rule[1]

        # 기본 파티션키 삽입
        df.insert(0, 'partition_key', df[key_rule[1]].map(lambda value: eval(key_rule[0] + '(str(value))')))  # extract_numType1(str(value))

    def insertPartitionKey(self, df, rule):
        rules = rule.split(':') # rule명:필드

        print('rules : {}'.format(rules))

        df.insert(0, 'partition_key', df[rules[1]].map(lambda value: eval(rules[0] + '(str(value))'))) # extract_numType2:ROUT_NO

        if len(rules) > 2: # 파티션키 로우 갯수 제한값이 있으면
            split_num = int(rules[2])
            
            for key, group in df.groupby('partition_key'):
                #print('len(group) : {}, split_num : {}'.format(len(group), split_num))

                if len(group) > split_num:
                    row_count = 0
                    add_num = 1

                    for i in group.index:
                        row_count = row_count + 1

                        if row_count > split_num:
                            partition_key = group._get_value(i, 'partition_key')
                            new_partition_key = '1' + ('%08d' % add_num) + partition_key[-1]
                            df._set_value(i, 'partition_key', new_partition_key)

                            #print('row_count : {}, partition_key : {}, new_partition_key : {}, group._get_value : {}'.format(row_count, partition_key, new_partition_key, df._get_value(i, 'partition_key')))

                            if row_count % split_num == 0:
                                add_num = add_num + 1

    def insertPartitionDate(self, df, rule):
        rules = rule.split(':')  # rule명:필드
        standardYMD = rules[2]

        print('rules : {}'.format(rules))

        if rules[2] == 'YMD':
            standardYMD = Date.curDateStr('%Y%m%d')

        df.insert(1, 'partition_date', df['partition_key'].map(lambda value: eval(rules[0] + '(\'' + standardYMD + '\', str(value))'))) # extract_fixDate1('20210528', value[-1])

if __name__ == '__main__':  # 프로그램의 시작점일 때만 아래 코드 실행
    # 파티션 키 : 파티션 키는 특정컬럼의 끝자리 숫자값 과 그외의 문자
    # 파티션 데이트 : 기준년월일(yyyymmdd) 픽스 시작일 ~ 끝날자([0-9], 기타문자) 나머지 시분초는 데이터 넣는 시점의 값으로

    csv_file_path = 'C:/Users/ff/Desktop/서울시관련/csv_convert'

    splitter = CsvSplitter(csv_file_path, 'ICC_MS_BMS_ROUT_COMP.csv', 'ICC_MS_BMS_ROUT_COMP.xml')
    splitter.splitCsv()

    """
    - 파티션 키 : 컬럼 끝자리 숫자 값 : [0-9] -> 대상값은 숫자여야 한다. 로우갯수로 제한을 둬서 파티션 키 생성
    - 파티션 데이트 : 기준년월일(yyyymmdd) 픽스 시작일 ~ 끝날자([0-9], 기타문자) 나머지 시분초는 데이터 넣는 시점의 값으로
    
    csv_file_path = 'C:/Users/ff/Desktop/서울시관련/csv_convert'
    table_info_xml_path = 'C:/Users/ff/Desktop/서울시관련/csv_convert/ICC_MS_BMS_ROUT_BUS.xml'

    splitter = CsvSplitter(csv_file_path, 'ICC_MS_BMS_ROUT_BUS.csv', 'ICC_MS_BMS_ROUT_BUS.xml')
    splitter.splitCsv()
    
    - 파티션 키 : 컬럼 끝자리 숫자 값 : [0-9] -> 대상값은 숫자여야 한다.
    - 파티션 데이트 : 기준년월일(yyyymmdd) 픽스 시작일 ~ 끝날자([0-9], 기타문자) 나머지 시분초는 데이터 넣는 시점의 값으로
    
    csv_file_path = 'C:/Users/ff/Desktop/서울시관련/csv_convert'
    table_info_xml_path = 'C:/Users/ff/Desktop/서울시관련/csv_convert/ICC_MS_BMS_ROUT.xml'

    splitter = CsvSplitter(csv_file_path, 'ICC_MS_BMS_ROUT.csv', 'ICC_MS_BMS_ROUT.xml')
    splitter.splitCsv()
    """