from lib.iris.exception.IrisException import PartitionKeyException
from lib.util.date import Date

# 컬럼 끝자리 숫자 값 : [0-9] -> 대상값은 숫자여야 한다.
def extract_numType1(value):
    if value[-1].isdigit():
        return '100000000' + value[-1]
    else:
        raise PartitionKeyException(value, 'extract_numType1 fail! not a digit!!')

# 컬럼 끝자리 숫자 or 모든문자: [0-9] or [모든문자] -> 대상값은 숫자 이거나 문자
def extract_numType2(value):
    if value[-1].isdigit():
        return '100000000' + value[-1]
    else:
        return '100000000_'

# 컬럼 끝자리 숫자 or 영문자 개별 : [0-9] or [a-zA-Z] -> 대상값은 숫자 나 영문자 여야한다.
def extract_numType3(value):
    if value[-1].encode().isalnum():
        return '100000000' + value[-1]
    else:
        raise PartitionKeyException(value, 'extract_numType2 fail! not a digit or alpha')

# 컬럼 끝자리 숫자 or 영문자 모두 : [0-9] or [영문자모두]
def extract_numType4(value):
    if value[-1].isdigit():
        return '100000000' + value[-1]
    elif value[-1].encode().isalpha():
        return '100000000_'
    else :
        raise PartitionKeyException(value, 'extract_numType3 fail! not a digit or alpha')

# 컬럼 끝자리 숫자 or 영문자 개별 or 그외의 문자 : [0-9] or [a-zA-Z] or [그외의문자]
def extract_numType5(value):
    if value[-1].encode().isalnum():
        return '100000000' + value[-1]
    else :
        return '100000000_'

def extract_fixDate1(yyyymmdd):
    return str(yyyymmdd) + Date.curDateStr('%H%M%S')