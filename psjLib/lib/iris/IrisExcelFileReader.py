import pandas as pd
from lib.iris.util.strUtil import cutStr

class IrisExcelFileReader:
    def __init__(self, excel_path, header, usecols, sheet_name, conf_dict):
        self.excel_path = excel_path
        self.header = header
        self.usecols = usecols
        self.sheet_name = sheet_name
        self.df = self.__readExcel()
        self.conf_dict = conf_dict
        #self.whole_data_dict = {}

    def __readExcel(self):
        return pd.read_excel(self.excel_path, header=self.header, usecols=self.usecols, sheet_name=self.sheet_name)

    # 대상여부 Y or ? 필터링
    def getTargetDf(self, fillna=""):
        return self.df[(self.df['대상여부'].str.lower() == 'y') | (self.df['대상여부'].str.lower() == '?')].fillna(fillna)

    def getWholeDict(self, targetDf):
        wholeDict = {}

        for key, group in targetDf.groupby(['OWNER', '테이블명']):  # OWNER 와 테이블명 으로 중복되지 않게 그룹
            col_list = []
            col_nm_list = []
            partDict = {'owner':key[0], 'eng_name':key[1], 'select_query':'', 'comment':'코멘트 내용', 'cols':col_list}
            is_init = True

            for index in group.index:
                if is_init:
                    partDict['kor_name'] = group._get_value(index, '테이블 한글명')
                    is_init = False

                col = self.__set_col(index, group)
                col_nm_list.append(col['col']['origin_eng_name'])
                col_list.append(col)

            partDict['select_query'] = ', '.join(col_nm_list)
            wholeDict[key[0] + '.' + key[1]] = partDict
        return wholeDict

    def __set_col(self, index, group):
        col = {}

        origin_eng_name = group._get_value(index, '컬럼명')
        origin_data_type = group._get_value(index, 'DATA_TYPE')

        col['select_origin_eng_name'] = self.__col_convert_str(origin_eng_name, origin_data_type)

        col['origin_eng_name'] = origin_eng_name
        col['origin_data_type'] = origin_data_type
        col['origin_kor_name'] = group._get_value(index, '컬럼 한글명')

        col['convert_eng_name'] = group._get_value(index, '표준용어 영문명')
        col['convert_kor_name'] = group._get_value(index, '② 표준용어')
        col['convert_data_type'] = group._get_value(index, '데이터타입')

        return {'col':col}

    def __col_convert_str(self, origin_eng_name, origin_data_type):
        convert_str = None
        cut_origin_data_type = cutStr(origin_data_type.lower(), '(')

        #print("cut_origin_data_type : {}".format(cut_origin_data_type))

        if cut_origin_data_type in self.conf_dict['irisDataType']['TEXT']:
            convert_str = self.conf_dict['rdbConvertStr']['TEXT'].replace('_col_', origin_eng_name)
        elif cut_origin_data_type in self.conf_dict['irisDataType']['DATE']:
            convert_str = self.conf_dict['rdbConvertStr']['DATE'].replace('_col_', origin_eng_name)
        elif cut_origin_data_type in self.conf_dict['irisDataType']['EXTRA']:
            convert_str = origin_eng_name + '(' + origin_data_type + ':구문확인 필요)'

        return convert_str