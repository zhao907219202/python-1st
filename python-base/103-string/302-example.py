width = int(input('Please input width: '))
price_width = 10
item_width = width - price_width
# - 左对齐 * 占位从元组读取
header_format = '%-*s%*s'
body_format = '%-*s%*.2f'
print('=' * width)
print(header_format % (item_width, 'Item', price_width, 'Price'))
print('-' * width)
print(body_format % (item_width, 'Apple', price_width, 0.4))
print(body_format % (item_width, 'Pears', price_width, 0.5))
print(body_format % (item_width, 'Cantaloupes', price_width, 1.92))
print(body_format % (item_width, 'Dried Apricots(16 oz.)', price_width, 8))
print(body_format % (item_width, 'Prunes(4 lbs', price_width, 12))
print('=' * width)
