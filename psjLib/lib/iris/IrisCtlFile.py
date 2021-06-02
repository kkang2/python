from lib.iris.util.strUtil import cutStr

class IrisCtlFile:
    def __init__(self, data_type_info, col_convert_func_info):
        self.data_type_info = data_type_info
        self.col_convert_func_info = col_convert_func_info

    def generateCtlFile(self, tbl_nm, cols_list, path):
        ctl_contents = self.__generateCtlContents(cols_list)

        print(ctl_contents)

        if len(ctl_contents) > 0:
            with open(path + '/' + tbl_nm + '_ctl', "w") as file:
                file.writelines(ctl_contents)
        else:
            print('ctl 파일을 만들 컬럼데이터 가 없습니다.')

    def __generateCtlContents(self, cols_list):
        ctl_contents = []

        for col_dict in cols_list:
            col_nm = col_dict['col']['convert_eng_name']
            origin_col_type = col_dict['col']['convert_data_type']

            print("col_nm : {}, origin_col_type : {}".format(col_nm, origin_col_type))

            cut_col_type = cutStr(origin_col_type.lower(), '(')

            if cut_col_type in self.data_type_info['NUMBER']:
                if origin_col_type.find(',') < 0:
                    ctl_contents.append(col_nm + ',' + self.col_convert_func_info['INT'] + '\n')
                else:
                    ctl_contents.append(col_nm + ',' + self.col_convert_func_info['REAL'] + '\n')
            else:
                ctl_contents.append(col_nm + ',' + self.col_convert_func_info['TEXT'] + '\n')

        return ctl_contents