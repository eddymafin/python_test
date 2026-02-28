# セイウチ演算子：式の中で変数に値を代入しながら、その値を同時に使用できる演算子
# 下記の記述を
# name = input('your name: ')
# if name:
#   print(f'hello! {name}')

# セイウチ演算子を使用すると
if name := input('your name: '):
 print(f'hello! {name}')
 
 numbers = [1,2,3,4,5,6,7]
 if(length := len(numbers)) >= 3:
   print(length)

# ユーザーが入力した値が、100以上の場合に実行
if (n := int(input('input number: '))) > 100:
  print(f'{n}の2倍: { n * 2}')

# qが入力されるまで、入力できる
while(line := input('入力：')) != 'q':
  print(f'入力: {line}')
