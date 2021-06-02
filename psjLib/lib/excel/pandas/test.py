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


"""
excel = rd.read_excel("C:/Users/ff/PycharmProjects/psjLib/data/excel/3.보도포장관리_시스템.xlsm", 0,
                   "A:Q", "1. 대상테이블")
print(excel.head(3))
"""
"""
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
"""

"""
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)
print(df)

print(df.index) # 인덱스 출력
print(df.columns) # 열 출력
print(df.values) # 값 출력
"""

"""
sr = pd.Series([17000, 18000, 1000, 5000], index=["피자", "치킨", "콜라", "맥주"])

print(sr)
print(sr.values)
print(sr.index)
"""