import datetime


def printLog(requestData):
    print()
    print('[ Current Time ] ', datetime.datetime.now())
    print('[ Filter Code ] ', requestData['isFilter'])
    print('[ Request Data ] ', requestData['message'])


def writeLog(requestData, answerdata):
    logfile = open('log.txt', 'w')

    logfile.write('[ Time ] ' + str(datetime.datetime.now()) + '\n')
    logfile.write('[ Reqeust ] ' + str(requestData['message']) + '\n')
    logfile.write('[ Response ] ' + str(answerdata) + '\n')

    logfile.close()
