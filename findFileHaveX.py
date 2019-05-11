# encoding: utf-8

import os
import os.path
rootdir = "/Users/melon/company/baiduproject"                                   # 指明被遍历的文件夹

# 定义函数
def printme(parent,filename):
	#源文件路径
	originPath = os.path.join(parent,filename)
	#打开源文件
	originFile = open(originPath, "r")
	content = originFile.read()
	#修正源内容
	if content.find('selectComponent') != -1:
		print originPath
	#关闭文件
	originFile.close()
	return;

for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    # for dirname in  dirnames:                       #输出文件夹信息
        # print "parent is:" + parent
        # print  "dirname is" + dirname
	for filename in filenames:                        #输出文件信息
		printme(parent,filename)