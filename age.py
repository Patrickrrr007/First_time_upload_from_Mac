age = input('請輸入年齡：')
#age = int('age')	不要加單引號
#全型的單引號 「」
#全型的雙引號	『』
#半型的單引號	“
#半型的單引號	’

age = int(age)
#因為原本input存到age的是字串
#必須做型別轉換
if age >= 20:
	print('你可以投票了')

