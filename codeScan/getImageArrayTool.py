# -*- coding: utf-8 -*-
import os

class GetImageTool(object):

    def __init__(self):
        self.imagearray = [];
        self.imageDic = {};

    # 遍历指定目录，显示目录下的所有文件名
    def eachFile(self,filepath):
        if os.path.isdir(filepath):
            # print("it's a directory")
            pathDir = os.listdir(filepath)
            for allDir in pathDir:
                if allDir == ".DS_Store":
                    continue
                child = os.path.join(filepath, allDir)
                # print(child)  # .decode('gbk')是解决中文显示乱码问题
                self.eachFile(child)
        elif os.path.isfile(filepath):
            lastPath = os.path.split(filepath)[1]
            suffix = os.path.splitext(lastPath)[1]
            lastPathName = os.path.splitext(lastPath)[0]
            if suffix ==".png"or suffix==".jpg":
                self.imagearray.append(lastPathName)
                self.imageDic[lastPathName]=filepath;
        else:
            print("it's a special file (socket, FIFO, device file)")
            print(filepath)


    def getImageArrayWithFilePath(self,path):
        self.eachFile(path)
        return self.imagearray



