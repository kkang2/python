import pandas as pd

# https://rfriend.tistory.com/450
def getTableInfos(df):
    allRowCount = len(df) # 값이 없는 행도 체크
    notNullRowCount = df.count()['테이블명'.strip()] # 값이 없는 행은 갯수에 포함 안됨
    targetTableCount = len(df[(df['대상여부'.strip()].str.lower() == 'y') | (df['대상여부'.strip()].str.lower() == '?')])
    nonTargetTableCount = len(df[df['대상여부'.strip()].str.lower() == 'n'])
    
    print("읽은 전체 행 : {0}, 값이 있는 전체 행 : {1}".format(allRowCount, notNullRowCount))
    print("전체 테이블 갯수 : {0}, 대상 테이블 갯수 : {1}, 비대상 테이블 갯수 : {2}"
          .format(targetTableCount + nonTargetTableCount, targetTableCount, nonTargetTableCount))

# "I ate {0} apples. so I was sick for {1} days.".format(number, day)
# "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)

def getTargetTable():
    pass