# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:41:48 2020

@author: PENG PIE

处理地面气象要素数据文件的正点降水资料
该文件为顺序数据文件，共3条记录，
第1条记录为本站基本参数，共34个字节；
第2条记录为器测项目，共262字节；
第3条记录为小时内分钟降水量，120个字节；
最后一条记录的后面加上“=<CR><LF>”，表示单站数据结束，
其他记录尾用回车换行“<CR><LF>”结束；
文件结尾处加“NNNN<CR><LF>”，表示全部记录结束。

所需的1小时降水位于第二条记录的第14个要素（用1个半角空格分隔），共4个字节，即第67-70个字符
存储各要素值不含小数点，记录单位为0.1mm，存储规定扩大10倍

若要素缺测或无记录，除有特殊规定外，则均应按约定的字长，每个字节位存入一个“/”字符

59134 242900 1180400 01394 01406 4
20190101020000 039 042 050 038 035 057 0116 020 052 025 091 0110 0000 0151 0153 0153 0140 0101 064 064 0143 110 0083 10134 10139 0103 10134 0152 //// //// //// //// //// 0210 0218 0152 0164 0101 0162 0151 0153 0159 //// //// //// //// 0000 10305 30000 30000 0101
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000=
F2101 242627 1180816 00159 ///// 4
20190101020000 /// /// /// /// /// /// //// /// /// /// /// //// 0000 //// //// //// //// //// /// /// //// /// //// ///// ///// //// ///// //// //// //// //// //// //// //// //// //// //// //// //// //// //// //// //// //// //// //// //// ///// ///// ///// ////
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000=

国家级自动站列表：
    厦门3个 59134,59130,59140
    泉州7个 58929,58931,58934,58935,59131,59133,59137
        安溪，九仙山，永春，德化，南安， 崇武，晋江
    漳州10个 58928,59122,59124,59125,59126,59127,59129,59320,59321,59322
        华安， 长泰， 南靖，平和，漳州，龙海，漳浦， 诏安，东山， 云霄
    
"""
#导入数据分析包
# import pandas as pd
# import numpy as np
import os
import sys
import getopt

from os import listdir, remove
from os.path import isfile, join, exists

EXPECTED_STATION_PRE = ['F2','F5','F6']     #限定厦门F2，泉州F5，漳州F6区域自动站
EXPECTED_STATION = ['58928','58929','58931','58934','58935',\
                    '59122','59124','59125','59126','59127','59129',\
                        '59130','59131','59133','59134','59137','59140',\
                            '59320','59321','59322']        #限定国家级自动站
###判断是否满足自动站列表########################################
def isMyStation(st):        
    ret = False
    
    for pre in EXPECTED_STATION_PRE:
        if st.find(pre) == 0:
            ret = True
            break
        
    if ret:
        return ret
    
    for station in EXPECTED_STATION:
        if st == station:
            ret = True
            break
        
    return ret

###坐标换算，度分秒=度+分/60+秒/3600########################################
def parseLocation(inVal):
    ss = inVal[-2:]
    mm = inVal[-4:-2]
    hh = inVal[:-4]
    v = ""
    
#    print("{}.{}.{}".format(hh,mm,ss))
    
    try:
        s = float(ss)/3600
        m = float(mm)/60
        h = float(hh)
        
        v = "{:.3f}".format(h + m + s)
#        print(v)
    except ValueError as ex:
        print("Invalid location value: " + inVal + ", " + str(ex))
        
    return v
    
###逐3行读取数据，导出要用的数据########################################    
def extractData(inFile, outFile, expectValue):
    f = open(inFile,'r')
    
    result = list()
    count = 0
    outRows = 0
    while True:
        count += 1
        
        line1 = f.readline()
        r1 = line1.split()
        line2 = f.readline()
        r2 = line2.split()
        line3 = f.readline()
        r3 = line3.split()
        if not line1:
            break
        
        station = r1[0]     #第一行第一个要素为站号
        
        if not isMyStation(station):
            if DEBUG_MODE:
                print("Not expected station: " + station)
            continue
        
        try:
            v = int(r2[13])
        except ValueError as ex:
            if DEBUG_MODE:
                print("{}, Line{}: invalid int value: {}".format(inFile, (count-1)*3+2, r2[13]))
            continue
                
        if(v<expectValue):
            if DEBUG_MODE:
                print("{}, value lower than threshhold: {}".format(inFile, v))
            continue
        
        outRows += 1
        if(outRows==1):
            fw = open(outFile, "a")
            
        row = ""
#        if c > 1:
#            row += "\n"
        row += r2[0]    #time
        row += " " + r1[0] # station
        row += " " + parseLocation(r1[1]) # lat
        row += " " + parseLocation(r1[2]) # lon
        row += " " + r1[3] # height
        row += " " + r2[13] # rain value
        row += "\n"
        if DEBUG_MODE:
            print("Line{}:{}".format(c, row))
        fw.write(row)
    
    f.close()
    if outRows>= 1:
        fw.close()
        print("{} => {} : {}".format(inFile, outFile, outRows))
    else:
        print("{} => {}".format(inFile, outRows))
    
    return outRows

def listDataFolder(dataPath):
    files = listdir(dataPath)
    for f in files:
        if isfile:
            print(f)

###判断是否为小时正点数据
def isHourFile(fileName):
    idx = fileName.find(".")
    if idx == -1:
        return False
    if fileName[idx-3:idx-1] == "00":
        return True
    return False

def printDebugInfo(msg):
    if DEBUG_MODE:
        print(msg)

def extractDataFolder(dataPath, outPath, v, removeExistingFile):
    files = listdir(dataPath)
    fileCounter = 0
    if not os.path.exists(outPath):
        os.mkdir(outPath)
    
    print("==== total files or dirs: " + str(len(files)) + " ====")

    for fileName in files:
        inFile = join(dataPath, fileName)
        if DEBUG_MODE:
            print("processing: " + inFile)

        if not isfile(inFile):
            if DEBUG_MODE:
                print("ignore director: " + fileName)
            continue

        if not isHourFile(fileName):
            if DEBUG_MODE:
                print("{} not at hour".format(fileName))
            continue

        outFile = join(outPath, fileName+".txt")
        if removeExistingFile and os.path.exists(outFile):
            if DEBUG_MODE:
                print("remove output file: " + outFile)
            remove(outFile)
        
        if extractData(inFile, outFile, v)> 0:
            fileCounter += 1

    print("total output files: " + str(fileCounter))

#datapath = 'D:/aws/ai'
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#fileNameStr = 'D:/aws/ai/AI201901010200.EFZ'
#DataDF = pd.read_csv(fileNameStr,encoding = "utf-8",dtype = str,sep = " ") 

#print(DataDF.head())



#for line in f:
#    line = f.readline()
#    print line
#    result.append(line)
#print result
#f.close()                

###默认执行路径，阈值，覆盖


def main(argv):
    dataFolder = './ai'
    outputFolder = './out'
    threshhold = 500
    overrideExisting = True
    debugMode = False

    usage = "-i <inputFolder> -o <outputFolder> -t <threshhold> -r <override> -d"
    try:
        opts, args = getopt.getopt(argv, "hi:o:t:r:d",["input","output","threshhold","override","debug"])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
            return
        elif opt in ("-i", "--input"):
            dataFolder = arg
        elif opt in ("-o", "--output"):
            outputFolder = arg
        elif opt in ("-t", "--threshhold"):
            threshhold = int(arg)
        elif opt in ("-r", "--override"):
            overrideExisting = bool(arg)
        elif opt in ("-d", "--debug"):
            debugMode = True

#    if(len(sys.argv)>=3):

    print("======================================================")
    print("data folder: " + dataFolder)
    print("output folder: " + outputFolder)
    print("threshhold: " + str(threshhold))
    print("override output files: " + str(overrideExisting))    
    print("Debug mode: " + str(debugMode))
    DEBUG_MODE = debugMode
    extractDataFolder(dataFolder, outputFolder, threshhold, overrideExisting)
    print("====================== done ==========================")

DEBUG_MODE = False
if __name__ == "__main__":
    main(sys.argv[1:])
       
#    parseLocation("500601")
    