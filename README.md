# threadingSpider
多线程爬虫的实现方式：

1.threadingSpider_type_1.py:创建10个子线程（task），分别把任务分配给10个线程
（1）.t.setDaemon(True) #将线程申明为守护线程，必须在start()方法执行之前设置，否则守护线程会被无限挂起.
