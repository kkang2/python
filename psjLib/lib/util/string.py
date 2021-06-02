# targetStr 전까지의 문자열을 돌려줌
def cutStr(originStr, targetStr):
    cutStr = ''
    findIndex = originStr.find(targetStr)

    #print(findIndex)

    if findIndex > -1:
        cutStr = originStr[:findIndex]
    else:
        cutStr = originStr

    return cutStr

"""
print(cutStr('VARCHAR(10)', '('))

testList = ['char', 'varchar', 'varchar2', 'nvarchar2']
numList = ['number']

if cutStr('VARCHAR(10)', '(').lower() in testList:
    print('use_date,to_text(?, null)')
else:
    print('dklfjsdklfjdkl')


if 'number' in numList:
    print('use_date,to_text(?, null)')
"""