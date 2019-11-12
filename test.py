#coding:utf-8
import os,sys,chardet
name = 'none'
action = 'none'
for index in range(len(sys.argv)):
	if((index+1) != len(sys.argv)):
		if(sys.argv[index] == '-fname' and sys.argv[(index+1)][0] != '-'):
			name = sys.argv[(index+1)]
			os.mkdir(name)
			# os.rmdir(name)
			name = name.decode('gbk').encode('utf-8')
			# print name
			# sys.stdout.write(("已创建")+name+("文件夹"))
			sys.stderr.write(("已创建")+name+("文件夹"))