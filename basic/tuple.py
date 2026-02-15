# tuple型
# 変更不可能なコレクションデータ型
# 複数の要素を一つの変数に格納するために使用する

# リストとの使い分け
# タプルは、作成時に必要なメモリだけを確保して、効率的に使用できる
# リストは、可変する可能性があるため、通常使用サイズの2倍くらいのメモリを確保している
# 上記のことから、タプルは定数で使用することがよさそう。座標、曜日

color = ('red', 'blue', 'yellow','red')

# 要素の追加。最後にカンマが必要
color = color + ('green',)

print(color)
# ダブルはあまりメソッドを使うことは無さそう
# 定数で使用されることが多いので
print(color.count('red'))


cordinates = (135, 35)

# アンパック：javascriptのスプレッド構文と似てる
longtitude, latitude = cordinates
print(longtitude, type(longtitude))
print(latitude, type(latitude))

# 辞書型のキーに指定することができる
countries = {cordinates: 'Japan'}

print(countries.get((135,35)))


