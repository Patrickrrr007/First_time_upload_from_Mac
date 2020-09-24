#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出"終於答對了"
#猜錯的話 要告訴他 比答案大/小

import random
x = input('請決定隨機數字範圍開始值：')
x = int(x)
y = input('請決定隨機數字範圍結束值：')
y = int(y)
g = random.randint(x, y)
count = 0

while True:
	count = count + 1
	guess_number = input('請猜數字：') 
	guess_number = int(guess_number)
	if g == guess_number:
		print('終於答對了')
		print('你輸入了', count ,'次')
		break
	elif g < guess_number:
		print('比答案小')
	elif g > guess_number:
		print('比答案大')	
		#print('你輸入了', count ,'次')
		#建議打在外面 就不用
	print('你輸入了', count ,'次')



