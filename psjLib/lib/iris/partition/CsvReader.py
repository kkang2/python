from logging import exception

import pandas as pd
from lib.iris.util.partition_key_util import *


dtype = eval("{'FDL_9':'str'}")

print(type(dtype))

df = pd.read_csv('C:/Users/ff/PycharmProjects/psjLib/data/csv/ICC_MS_BMS_ROUT_short.csv',
                 encoding='utf-8', header=0, sep='', dtype=dtype) # 숫자 앞에 0 짤리는걸 방지하기 위해 dtype값을 줌

print(df.head(5))
print(df['FDL_9'])

#df['partitionKey'] = df['FDL_I1'].map(lambda value: extract_numType1(str(value)))
df.insert(0, 'partition_key', df['FDL_I1'].map(lambda value: extract_numType1(str(value))))
df.insert(1, 'partition_date', df['partition_key'].map(lambda value: extract_fixDate1('20210528', value[-1])))

print(df.head(5))

for key, group in df.groupby('partition_key'):
    #print("key :{}".format(key))
    print("group :{}".format(group))
    
    group.to_csv('C:/Users/ff/PycharmProjects/psjLib/data/output/ICC_MS_BMS_ROUT_output.csv', sep='', header=True, index=False)

    break;

#print(extract_numType1('1747474'))


#df['partitionKey'] = df['FDL_I1'].str.












