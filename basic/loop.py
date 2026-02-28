# for range
# for i in range(10):
#   print(i)
#   print('_' * 10)
 
#  2-19までを3つ飛ばしで ループ
for i in range(2, 20, 4):
  print(i)
  print('_' * 10)
  
list_a = list(range(2, 30))
print(list_a, type(list_a))

# 同じ処理を10回実行する　アンダースコア＿の場合は、同じ処理を実行することを意味し、変数＿は中で利用しない。暗黙のルール
for _ in range(10):
  print('same')

# ループでの取り出し方
samples = ['a', 'b', 'c', 'd']
for sample in samples:
  print(sample)
  
animal = {
  'category': 'dog',
  'name': 'boss'
  
}
# dictionary型の取り出し方
for key in animal:
  print(key, animal[key])

for value in animal.values():
  print(value)
  
for key, value in animal.items():
  print(key, value)
  
  
# enumerate:インデックスと要素を同時に取得できる関数
fruits = ['apple', 'pine', 'orange']
print(list(enumerate(fruits)))

for index, fruit in enumerate(fruits):
  print(f'index: {index}')
  print(f'fruit: {fruit}')
  
# zip:複数のリストを同じ位置の要素でまとめる関数
class_a_members = ['Taro', 'Hanako', 'Jiro']
class_b_members = ['Wakame', 'Shiro']
# ただし、小さい方の要素数でしかループされない。何に使うのか。。
for a, b in zip(class_a_members,class_b_members):
  print(f'a: {a}, b: {b}')
  
  
# while
count = 0
while count < 10:
  print(count)
  count += 1
  
