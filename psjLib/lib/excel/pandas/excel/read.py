import pandas as pd

# path : 엑셀파일 경로+파일명
# header : 컬럼명이 있는 행 위치(0부터 시작), 엑셀에 컬럼명이 없을때 컬럼명을 명시적으로 지정하려면 header=None 로 하고 names=리스트 형태로 줌
            # 엑셀에 컬럼명이 있는경우 header=0 로 하고 names=리스트 형태로 줌
# sheet_name : 읽을 시트이름
# usecols : 읽어올 컬럼명(A열부터 시작)
def read_excel(path, header, usecols, sheet_name):
    return pd.read_excel(path, header=header, usecols=usecols, sheet_name=sheet_name)

