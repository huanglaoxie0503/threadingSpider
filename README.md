# threadingSpider
多线程爬虫的实现方式：

方法一：threadingSpider_type_1.py:创建10个子线程（task），分别把任务分配给10个线程

方法二：threadingSpider_type_2.py：创建10个线程，任务自己实现分配。

（1）t.setDaemon(True) #将线程申明为守护线程，必须在start()方法执行之前设置，否则守护线程会被无限挂起.

网站：https://credit.justice.gov.cn/subjects.jsp?typeId=10d341aea6674146b36dd23c25090f04&page=1
