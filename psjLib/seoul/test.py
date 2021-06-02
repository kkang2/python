import string

import yaml
from lib.util.date import Date
from lib.iris.util.partition_key_util import *

print(ord('A')-55)
print(ord('Z')-55)

print(ord('a')-61)
print(ord('z')-61)


print(type(ord('가')))

print('@'.encode().isalpha())
print('a'.encode().isalpha())


"""
print('20210528'[:4])
print('20210528'[4:6])
print('20210528'[6:8])

print('20210528'[:4].lstrip('0'))
print('20210528'[4:6].lstrip('0'))
print('20210528'[6:8].lstrip('0'))

print(Date.curDateStr('%H시 %M분 %S초'))
"""


"""
print(extract_fixDate1('20210528', 0))
print(extract_fixDate1('20210528', 1))
print(extract_fixDate1('20210528', 9))


print('a'.isalnum())
print('규'.encode().isalnum())
print('가'.encode().isalpha())
print(string.ascii_lowercase)
print(type(string.ascii_lowercase))
"""



"""
# conf.yml 파일 읽기
with open('../data/conf/iris_partition_conf.yml', encoding='UTF8') as cf:
    conf = yaml.load(cf, Loader=yaml.FullLoader)


print(conf['irisPartitionKeyType'])
"""