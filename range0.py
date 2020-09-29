#range 範圍
#python內建功能：清單產生器
import random

range(5)
#0, 1, 2, 3, 4

range(7)
#0~6
#都會從0開始算

for i in range(100):
	r = random.randint(1, 100)
	print('這是第', i + 1, '產生隨機數：', r)



#Q:如何產生不重複的隨機數？
