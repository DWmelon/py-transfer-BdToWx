# encoding: utf-8

import os
import os.path
rootdir = "/Users/melon/company/baiduproject"                                   # 指明被遍历的文件夹
keyword = "selectComponent"

# 定义函数
def printme(parent,filename):
	#源文件路径
	originPath = os.path.join(parent,filename)
	#打开源文件
	try:
		originFile = open(originPath, "r")
	except IOError:
    		return
	content = originFile.read()
	#修正源内容
	if content.find(keyword) != -1:
		print originPath
	#关闭文件
	originFile.close()
	return;

str = raw_input("输入 需要搜索的目录 和 关键词\n比如:\n/Users/melon/company/baiduproject selectComponent\n请输入：\n")
paths = str.split(' ')
if len(paths) != 2 :
	print "输入有误，请确认是否为路径与关键词，中间用一个空格隔开"
	os._exit(0)
rootdir = paths[0]
keyword = paths[1]
for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    # for dirname in  dirnames:                       #输出文件夹信息
        # print "parent is:" + parent
        # print  "dirname is" + dirname
	for filename in filenames:                        #输出文件信息
		printme(parent,filename)
