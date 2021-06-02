from lib.iris.exception.IrisException import PartitionKeyException
from lib.util.date import Date

# 기준년월일(yyyymmdd) + 나머지 시분초는 데이터 넣는 시점의 값으로
def extract_fixDate1(yyyymmdd):
    return str(yyyymmdd) + Date.curDateStr('%H%M%S')

# 기준년월일(yyyymmdd) 부터 시작일 ~ 끝날자([0-9], 영문자, 기타문자) 나머지 시분초는 데이터 넣는 시점의 값으로
def extract_fixDate2(yyyymmdd, value):
    yyyy, mm, dd, char = extract_common_data(yyyymmdd, value)

    if char.isdigit():
        add_count = int(char)
    elif char.encode().isalpha():
        asciiNum = ord(char)

        if asciiNum >= 32 or asciiNum <= 57: # A~Z
            add_count = asciiNum - 55 # 10~35
        else: # a~z
            add_count = asciiNum - 61 # 36~61
    else:
        add_count = 62

    yyyymmdd = Date.addDayFromFixDate(yyyy, mm, dd, add_count).strftime('%Y%m%d')

    return yyyymmdd + Date.curDateStr('%H%M%S')

# 기준년월일(yyyymmdd) 부터 시작일 ~ 끝날자([0-9], 모든문자) 나머지 시분초는 데이터 넣는 시점의 값으로
def extract_fixDate3(yyyymmdd, value):
    yyyy, mm, dd, char = extract_common_data(yyyymmdd, value)

    if char.isdigit():
        add_count = int(char)
    else:
        add_count = 10

    yyyymmdd = Date.addDayFromFixDate(yyyy, mm, dd, add_count).strftime('%Y%m%d')

    return yyyymmdd + Date.curDateStr('%H%M%S')

# 기준년월일(yyyymmdd) 하나의 값으로 숫자값(0~9) : 2시간씩 20시간 그외에 문자는
def extract_fixDate3(yyyymmdd, value):
    yyyy, mm, dd, char = extract_common_data(yyyymmdd, value)

    if char.isdigit():
        add_count = int(char)
    else:
        add_count = 10

    yyyymmdd = Date.addDayFromFixDate(yyyy, mm, dd, add_count).strftime('%Y%m%d')

    return yyyymmdd + Date.curDateStr('%H%M%S')

def extract_common_data(yyyymmdd, value):
    return (yyyymmdd[:4], yyyymmdd[4:6].lstrip('0'), yyyymmdd[6:8].lstrip('0'), value[-1])