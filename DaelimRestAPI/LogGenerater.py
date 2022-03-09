import datetime


def printLog(requestData, answerdata):
    print()
    print('[ Current Time ] ', datetime.datetime.now())
    print('[ Filter Code ] ', requestData['isFilter'])
    print('[ Request Data ] ', requestData['message'])
    print('[ Response Data ] ', answerdata)


def writeLog(requestData, answerdata):
    logfile = open('log.txt', 'a', encoding='utf-8')

    logfile.write('[ Time ] ' + str(datetime.datetime.now()) + '\n')
    logfile.write('[ Reqeust ] ' + str(requestData['message']) + '\n')
    logfile.write('[ Response ] ' + str(answerdata) + '\n')

    logfile.close()
