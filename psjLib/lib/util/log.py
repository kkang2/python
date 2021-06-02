import yaml, os
import logging
import logging.config

def getLogger(name):
    logger = logging.getLogger(name)

    if len(logger.handlers) > 0:
        return logger  # Logger already exists
    else:
        setLogConfig()

    #print(logger)
    #print(logger.handlers)

    return logger

def setLogConfig():
    print('로그 컨피그 호출')

    log_conf_path = '../conf/log_conf.yml'

    if os.path.exists(log_conf_path):
        with open(log_conf_path, 'rt', encoding='utf-8') as f:
            logging.config.dictConfig(yaml.load(f, Loader=yaml.FullLoader))
    else:
        print("로그 컨피그 파일 존재하지 않음")
        #logging.basicConfig(level=logging.INFO)