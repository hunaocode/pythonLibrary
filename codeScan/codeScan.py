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
        for str in imageArray:
            p1 = r'%s' % str
            pattern1 = re.compile(p1)  # 同样是编译
            matcher1 = re.search(pattern1, line)  # 同样是查询
            if matcher1:
                imageArray.remove(str)
                print("在%s中找到了%s" % (filename,str))
            else:
                pass
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

    fileName = '/Users/huguobin/Desktop/codeScan'
    imageTool = GetImageTool()
    imageArray = imageTool.getImageArrayWithFilePath(fileName)
    for key,value in imageTool.imageDic.items():
        print(key,value)
    imageArray2 = eachFile(fileName,imageArray)
    for str in imageArray2:
        path = imageTool.imageDic.get(str)
        print("删除%s路径下的%s图片" % (path,str))
        os.remove(path)
