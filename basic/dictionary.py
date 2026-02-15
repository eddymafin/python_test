mount = {'name': 'Fuji', 'prefecture': 'Shizuoka', 'level':2 }

# キー指定で、値を表示
print(mount['name'])

# getメソッドで、存在しないものが指定された場合は、noneで返却される
# また、第2引数に存在しなかった場合に返却する値を設定できる
print(mount.get('nam', 'does not exist'))

# キーの一覧を表示
print(mount.keys())
# 値の一覧を表示
print(mount.values())
# キーと値の一覧を表示
print(mount.items())

# for文でキーと値を出力
for key, value in mount.items():
  print('key = {}, value = {}'.format(key,value))
 
#  キーが存在する場合のみ出力できる。キーが存在しない場合は、実行されない
if 'name' in mount:
  print('名前は{}'.format(mount['name']))
  
  
  tmp_dict = {
    'comment': 'not interested just one time is enough',
    'level': 3
  }
  
  # dictionaryの更新
  mount.update(tmp_dict)
  print(mount)
  # 最後の要素を取り出す。あんまり使わない？
  value = mount.popitem()
  print(value)
  print(mount)
  
  # 指定した要素を取り出す：pop
  value = mount.pop('level')
  print(mount)
  print(value)
  
  # 全削除
  mount.clear()
  print(mount)
  