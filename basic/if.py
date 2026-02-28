age = 20

# 数値型の場合、0以外はtrue
if age:
  print(f'ageの値: {age}')
  
msg = ''
# 文字列は、空文字、リスト、辞書、タプル、セットは、falseと評価される
if msg: 
  print(f'msgの中身は: {msg}')
  
check_age = 18  
if check_age >=18:
  print('成人です')
  
# elifなので注意  
color = 'yellow'
if color == 'blue':
  print('go ahead')
elif color == 'red':
  print('stop!!')
else:
  print('whatever')
  
role = 'soldier'
level = 20

if role == 'soldier' or level <= 20:
  print('you are not ready')
  
if role == 'general' and level > 20:
  print('you can go ahead')
  
if role != 'soldier' and role != 'general':
  print('you are not qualificated')
  
# NoneTypeクラスのオブジェクト。Noneのいう値しかない
a = None
# a == Noneという書き方もできるけど、慣習的に効率的なので、こっちのほうがいいらしい
if a is None:
  print('aはNoneです')
  
# isinstance
age = 25
name = 'yamada'
print(isinstance(age, int))
print(isinstance(name, str))

if isinstance(age, int) and age > 20:
  pass

# 三項演算子
# 他の言語と記述の仕方が違う
status = 'adult' if age >=18 else 'child'
print(status)


# allとany 反復可能なオブジェクトのみ使用できる。list tuple setなど
# allはすべてtrueの場合にtrueとなる
if all((True, 10, 'a')):
  print('すべてtrueの場合')

ages = [19, 21, 18, 25]
age_over_18 = [age >= 18 for age in ages]
print(age_over_18)
print(all(age_over_18))

if any ([10 < 0, 5, 0]):
  print('anyの中の処理')

