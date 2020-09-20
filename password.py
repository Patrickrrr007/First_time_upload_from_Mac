#自己打的
y = 1
while y <= 3:
 	passsword = input('請輸入密碼：')
 	if passsword == 'a1234567':
 		print('密碼正確！')
 	else:
 		print('請再輸入一次')
 		print('密碼錯誤！你還能輸入' , y, '次')
 		y = y + 1
print('請聯絡客服中心')

