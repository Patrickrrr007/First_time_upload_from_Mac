#自己打的
''' y = 1
while y <= 3:
 	passsword = input('請輸入密碼：')
 	if passsword == 'a1234567':
 		print('密碼正確！')
 	else:
 		print('請再輸入一次')
 		print('密碼錯誤！你還能輸入' , y, '次')
 		y = y + 1
print('請聯絡客服中心') '''

#------------------------------------
#老師版本

password = 'a1234567'
#建議先宣告進去
x = 3

while True:
	x = x - 1
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('成功登入')
		break
	else:
		print('密碼錯誤你還能輸入' , x, '次')
		if x == 0:
			break
