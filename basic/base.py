# name = input('your name?')
# comment = input('your comment')
# print(name)

# format関数
# print('your name is {}, {}'.format(name, comment))

# print(f'name is = {name}')

# Dictionary


mountain = {'name': 'Fuji', 'prefecture': 'Shizuoka', 'level':2 }

# キー指定で、値を表示
print(mountain['name'])

# getメソッドで、存在しないものが指定された場合は、noneで返却される
# また、第2引数に存在しなかった場合に返却する値を設定できる
print(mountain.get('nam', 'does not exist'))

# キーの一覧を表示
print(mountain.keys())
# 値の一覧を表示
print(mountain.values())
# キーと値の一覧を表示
print(mountain.items())

# for文でキーと値を出力
for key, value in mountain.items():
  print('key = {}, value = {}'.format(key,value))
 
#  キーが存在する場合のみ出力できる。キーが存在しない場合は、実行されない
if 'name' in mountain:
  print('名前は{}'.format(mountain['name']))
