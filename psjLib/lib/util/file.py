from pathlib import Path

#폴더안의 파일명 리턴
def getFilePathList(folderPath, pattern='*'):
    return Path(folderPath).glob(pattern)
