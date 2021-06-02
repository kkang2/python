import pandas as pd
import read as rd

excel = rd.read_excel("C:/Users/ff/PycharmProjects/psjLib/data/excel/3.보도포장관리_시스템.xlsm", 0, "A:Q", "1. 대상테이블")

print(excel.loc[[0, 1]])
#print(excel)