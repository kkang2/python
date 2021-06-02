import datetime as dt

class Date:
    @staticmethod
    def curDateStr(pattern):
        return dt.datetime.now().strftime(pattern)

    @staticmethod
    def addDayFromFixDate(yyyy, mm, dd, addCount):
        return (dt.datetime(int(yyyy), int(mm), int(dd)) + dt.timedelta(days=int(addCount)))


"""
%Y : 앞의 빈자리를 0으로 채우는 4자리 연도 숫자
%m :앞의 빈자리를 0으로 채우는 2자리 월 숫자
%d : 앞의 빈자리를 0으로 채우는 2자리 일 숫자
%H : 앞의 빈자리를 0으로 채우는 24시간 형식 2자리 시간 숫자
%M : 앞의 빈자리를 0으로 채우는 2자리 분 숫자
%S : 앞의 빈자리를 0으로 채우는 2자리 초 숫자
"""