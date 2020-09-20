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
		print('密碼錯誤!')
		if x > 0:
			print('你還能輸入', x, '次')
		else:
			print('沒機會嘗試了喔 請聯絡客服')
			break

		
