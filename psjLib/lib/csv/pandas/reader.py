import pandas as pd
# sep="\t" 구분자 지정해 줄수 있음
# header=None csv 파일 1행에 컬럼명이 없을때 컬럼명을 0부터 자동으로 생성
# names=['이름1', '이름2'] 컬럼명을 명시적으로 지정해 줄수 있음
# csv 파일의 1행에 컬럼명이 있는데 이 컬럼명을 수정하고 싶은 경우 header=0 으로 지정하고 names에 값을 넣어준다


#df = pd.read_csv('C:/Users/ff/PycharmProjects/psjLib/data/csv/subway_day.csv', encoding='utf-8')

#print(df)
#print(df.index)

df = pd.read_csv('C:/Users/ff/Desktop/data_load/CARD_SUBWAY_MONTH_202101.csv', encoding='utf-8'
                 , header=1, names=[0, 1, 2, 3, 4, 5, 6]).drop(6, axis=1)

print(df.head(5))

# 사용일자별 CSV 파일 생성
for key, group in df.groupby(0):
    #print(key)

    sorted_group = group.sort_values(by=1)
    group.to_csv('C:/Users/ff/Desktop/data_load/output/' + str(key) + '.csv'
                 , encoding='utf-8', header=False, index=False)

    break
    #print(group)



