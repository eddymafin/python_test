
# break:ループの途中で、即座終了
# continue:現在の反復処理をスキップして、ループの先頭にもどる

for i in range(20):
  if i == 10:
    break
  if i % 3 == 0:
    continue
  print(i)
print('_' * 10)

num = 0
while num < 10:
  num += 1
  if num % 2 == 0:
    continue
  print(num)   
