# encoding: utf-8

import os
import os.path
rootdir = "/Users/melon/company/baiduproject"                                   # 指明被遍历的文件夹
newdir = "/Users/melon/company/ttproject"
type = ""

def verifyWordAndModify(content):
    	# 替换API关键词
    	if type == "1":
        	content = content.replace('swan','wx')
        	content = content.replace('s-for','wx:for')
        	content = content.replace('s-for-item','wx:for-item')
        	content = content.replace('s-for-index','wx:for-index')
        	content = content.replace('s-for-index','wx:for-index')
        	content = content.replace('s-if','wx:if')
        	content = content.replace('s-elif','wx:elif')
        	content = content.replace('s-else','wx:else')
    	if type == "2":
        	content = content.replace('swan','tt')
        	content = content.replace('s-for','tt:for')
        	content = content.replace('s-for-item','tt:for-item')
        	content = content.replace('s-for-index','tt:for-index')
        	content = content.replace('s-for-index','tt:for-index')
        	content = content.replace('s-if','tt:if')
        	content = content.replace('s-elif','tt:elif')
        	content = content.replace('s-else','tt:else')
	return content

def verifyPathAndModify(path):
	# 重命名文件
	if type == "1":
		path = path.replace('.swan','.wxml')
		path = path.replace('.css','.wxss')
	if type == "2":
		path = path.replace('.swan','.ttml')
		path = path.replace('.css','.ttss')
	return path

# 定义函数
def printme(parent,filename):
	#源文件路径
	originPath = os.path.join(parent,filename)
	#打开源文件
	originFile = open(originPath, "r")
	#目标文件路径
	newPath = newdir + originPath.replace(rootdir,'') 
	#目标文件目录路径
	newDir = newPath.replace(filename,"")
	#修正文件名
	newPath = verifyPathAndModify(newPath)
	#创建目录
	if not os.path.exists(newDir):
		os.makedirs(newDir)
	#读取源文件内容
	newFile = open(newPath, "w")
	fileContent = originFile.read()
	#修正源内容
	fileContent = verifyWordAndModify(fileContent)
	#写入到新文件中
	newFile.write(fileContent)
	#关闭文件
	originFile.close()
	newFile.close()
	return;

str = raw_input("输入 源项目根目录 和 转后的存放目录\n比如:\n/Users/melon/company/baiduproject /Users/melon/company/wxproject\n请输入：\n")
paths = str.split(' ')
if len(paths) != 2 :
	print "输入有误，请确认是否为两个路径，中间用一个空格隔开"
	os._exit(0)
rootdir = paths[0]
newdir = paths[1]
type = raw_input("输入 转化类型 1：转微信 2：转头条\n")
if type != "1" and type != "2":
    print "输入有误，请输入1或者2"
    os._exit(0)
for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    # for dirname in  dirnames:                       #输出文件夹信息
        # print "parent is:" + parent
        # print  "dirname is" + dirname
	for filename in filenames:                        #输出文件信息
            print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
            if filename == "project.config.json":
                continue
            printme(parent,filename)
