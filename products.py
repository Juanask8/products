products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = [name, price]
	products.append(p)
print(products)
print(products[1][0])


for product in products:
	print(product[0], '的價格是', product[1])

with open('products.csv', 'w', encoding='utf-8') as f:  # with 檔案讀取
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') # ,做分隔 \n換行


