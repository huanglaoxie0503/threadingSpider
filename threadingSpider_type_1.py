import threading
from lxml import html
import requests
import re
import random
import chardet
import time
import pandas
from openpyxl import Workbook
from Common import user_agent

pageNum=1

def getHtml(url):
	headers={
		'User-Agent':random.choice(user_agent.USER_AGENTS)
	}
	response=requests.get(url,headers=headers).text
	time.sleep(random.randint(0,5))
	return response


def etreeHtml(txtHtml):
	tree=html.fromstring(txtHtml)
	results=tree.xpath('//ul[@class="multi-list"]/li')
	names=results[0].xpath('//div[@class="data"]/h3/text()')
	Numbers=results[0].xpath('//div[@class="data"]/p[@class="data-info"][1]/text()')
	Office=results[0].xpath('//div[@class="data"]/p[@class="data-info"][2]/text()')


	for n in range(len(names)):
		data=[(names[n],Numbers[n],Office[n])]
		#print(data)
		dataWrite=pandas.DataFrame(data)
		dataWrite.to_csv(r'E:\python\Reuslt\laws\上海律师_2.csv',index=False,header=False,mode='a+')


def run(startPage,endPage):
	try:
		for pageNo in range(startPage,endPage):
			url='https://credit.justice.gov.cn/subjects.jsp?typeId=10d341aea6674146b36dd23c25090f04&page={}'.format(pageNo)
			print('正在抓取第{}页'.format(pageNo))
			print('-------------------')
			html=getHtml(url)
			etreeHtml(html)
	except Exception as e:
		print('error:'.format(pageNo))
	finally:
		pass


def task1():
	print('task1 start......')
	run(1,700)
	print('task1 eng......')

def task2():
	print('task2 start......')
	run(700,1400)
	print('task2 end......')

def task3():
	print('task3 start......')
	run(1400,2100)
	print('task3 eng......')

def task4():
	print('task4 start......')
	run(2100,2800)
	print('task4 end......')

def task5():
	print('task5 start......')
	run(2800,3500)
	print('task5 eng......')

def task6():
	print('task6 start......')
	run(3500,4200)
	print('task6 end......')

def task7():
	print('task7 start......')
	run(4200,4900)
	print('task7 eng......')

def task8():
	print('task8 start......')
	run(4900,5600)
	print('task8 end......')
def task9():
	print('task9 start......')
	run(5600,5841)
	print('task9 end......')


def main():
	print('多线程爬虫方法一')
	starttime=time.time() #记录开始时间
	threads=[] #创建线程列表，存储创建的子线程
	th1=threading.Thread(target=task1)#创建第一个子线程，子线程的任务是调用task1函数
	threads.append(th1)#将子线程添加到线程列表

	th2=threading.Thread(target=task2) #创建第二个子线程
	threads.append(th2) #将子线程添加到线程列表

	th3=threading.Thread(target=task3)
	threads.append(th3)

	th4=threading.Thread(target=task4)
	threads.append(th4)

	th5=threading.Thread(target=task5)
	threads.append(th5)

	th6=threading.Thread(target=task6)
	threads.append(th6)

	th7=threading.Thread(target=task7)
	threads.append(th7)

	th8=threading.Thread(target=task8)
	threads.append(th8)

	th9=threading.Thread(target=task9)
	threads.append(th9)

	for t in threads:#遍历线程列表
		t.setDaemon(True) #将线程申明为守护线程，必须在start()方法执行之前设置，否则守护线程会被无限挂起
		t.start() #启动子线程

	for t in threads:
		t.join()

	endtime=time.time()#记录程序结束时间
	totaltime=endtime-starttime #计算机执行耗时

	print('耗时:{0:.5f}秒'.format(totaltime))#格式化输出耗时
	print('End')#结束


if __name__=='__main__':
	main()




