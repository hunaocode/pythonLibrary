#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

# 遍历指定目录，显示目录下的所有文件名
from getImageArrayTool import GetImageTool


def eachFile(filepath,imageArray):
    if os.path.isdir(filepath):
        #print("it's a directory")
        pathDir = os.listdir(filepath)
        for allDir in pathDir:
            if allDir==".DS_Store":
                continue
            child = os.path.join(filepath,allDir)
            #print(child)  # .decode('gbk')是解决中文显示乱码问题
            eachFile(child,imageArray)
    elif os.path.isfile(filepath):
        suffix =  os.path.splitext(filepath)[1]
        if suffix =='.h'or suffix =='.m' or suffix =='.storyboard' or suffix =='.xib':
            #print("it's a normal file")
            #print(filepath)
            readFile(filepath,imageArray)
    else:
        print("it's a special file (socket, FIFO, device file)")

    return imageArray

# 读取文件内容并打印
def readFile(filename,imageArray):
    f = open(filename, 'r')
    for line in f.readlines():
        find = False
        for str in imageArray:
            if str in line:
                find = True
                print("在%s中找到了%s" % (filename,str))
                imageArray.remove(str)
                break
            else:
                pass
            # p1 = r'%s' % str
            # pattern1 = re.compile(p1)
            # matcher1 = re.search(pattern1, line)  # 查询
            # if matcher1:
            #     find = True
            #     print("在%s中找到了%s" % (filename,str))
            #     imageArray.remove(str)
            #     break
            # else:
            #     pass
        if find:
            break
        #print(line.strip())
    f.close()
# 输入多行文字，写入指定文件并保存到指定文件夹
def writeFile(filename):
    fopen = open(filename, 'w')
    print("\r请任意输入多行文字( 输入 .号回车保存)")
    while True:
        aLine = input()
        if aLine != ".":
            fopen.write('%s%s' % (aLine, os.linesep))
        else:
            print("文件已保存!")
            break
    fopen.close()

if __name__ == '__main__':

    fileName = '/Users/huguobin/Desktop/JD4iPhone6'
    imageTool = GetImageTool()
    imageArray = imageTool.getImageArrayWithFilePath(fileName)
    imageSet = set(imageArray)
    print("在工程中共扫描到到%d张图片" % len(imageSet))
    # for str in imageArray:
    #     print(str)
    # for key,value in imageTool.imageDic.items():
    #     print(key,value)
    imageArray2 = eachFile(fileName,imageSet)
    if len(imageArray2):
        for str in imageArray2:
            path = imageTool.imageDic.get(str)
            print("未使用%s路径下的%s图片" % (path, str))
            # print("删除%s路径下的%s图片" % (path,str))
            # os.remove(path)
    else:
        print("未发现没有使用的图片")
