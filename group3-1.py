gkey = [
    [5, 4, 0, 1, 3, 6, 2,7],   #gkey1 康similarityユーザ順
    [2, 1, 5, 6, 3, 0, 4,7],   #gkey2
    [2, 5, 1, 3, 4, 0, 6,7]   #gkey3
]
# print(gkey)

len_i = len(gkey)      # 3  行数：教員のグループキーワード数
len_j = len(gkey[0])   # 7　列数：Similarityの高いユーザID順

group=[[] for i in range(len_i)]  #初期化

for j in range(len_j):  #ユーザ数分繰り返し
    i = j % len_i
    top = gkey[i][0]    #左側=Similarityの高い順からユーザを取出
    group[i].append(top)    #教員のグループキーワードにユーザをアサイン
    for k in range(len_i):  #それぞれのグループキーワードを対象
        gkey[k].remove(top)  #アサインしたユーザを削除

print(group)  #グループキーワードへのアサイン結果
#print(gkey)   #すべてがアサインされると空リストとなる