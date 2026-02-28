# セット
# 重複して値をいれることができない配列みたいな感じ.
# ただ、集合とかベン図とかの、和集合とか、積集合とか、そういうものを求めたいときのメソッドが用意されている
# また順番は保持されない
# 集合とかセットのものを作りたいときに、使用する。


set_a = {'a', 'b', 'c','d','a'}

# 重複したaは取り除かれる
print(set_a)

# 要素があるかのboolean
print('e' in set_a)

# 要素がないかのboolean
print('e' not in set_a)

# 要素の数をcount
print(len(set_a))

# 要素の削除：要素のないものが指定されるとエラーになる
set_a.remove('a')
print(set_a)

# 要素の削除：要素のないものが指定されてもエラーにならない
set_a.discard('e')


# 集合演算
s = {'a', 'b', 'c' , 'd' }
t = {'c', 'd', 'e' , 'f' }

# 和集合：sとtのどちらにも含まれる要素
u = s | t
# u = s.union(t)
print(u ,type(u))

# 積集合：sとtの両方に含まれる要素
i = s & t
# i = s.intersection(t)
print(i ,type(i))

# 差集合：sに含まれtに含まれない要素
diff = s - t
# diff = s.difference(t)
print(diff, type(diff))

# 対称差：sまたはtのどちらか一方にのみ含まれる要素

sym_diff = s ^ t
# sym_diff = s.symmetric_difference(t)
print(sym_diff)

d = {'apple', 'banana'}
e = {'apple', 'banana', 'lemon'}
# subeset:dがeの部分集合かどうか
subset1 = e <= d
subset2 = d <= e
print(subset1, 'subset1')
print(subset2, 'subset2')
print(e.issubset(d))


# superset:dがeの上位集合かどうか
# eの要素をすべて含んでいるかどうか
superset1 = d >= e
superset2 = e >= d
print(superset1, 'superset1')
print(superset2, 'superset2')
print(d.issuperset(e))


# setのよくある使い方
# 重複の削除
# リストの要素をsetに変換して、listに戻す
# for文でループするより早い
numbers = [1,2,2,2,3,3,3,4,5,6]
numbers = list(set(numbers))
print(numbers)

# 高速処理
# setは中のデータにすばやくアクセスができるようになっている
# large_list = list(range(100000)) 
large_list = set(range(100000)) 
test_number = 99999

import time

start = time.time()
# この処理に何秒かかったか計算
result = test_number in large_list
print(result)

end = time.time()
# 同じ処理だけど、setのほうがはるかに早く処理ができる
print('検索時間: ', end - start)


