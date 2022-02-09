#グループKeywordに対する学生ランキングを求めた結果から、グループを生成するプログラム　2022/1/11 Y.Tokiwa
#アルゴリズムが見つからなかったため、参考文献によらず独自開発した。
#課題：ボストン方式　かつ　Similarityの絶対値が反映されない。

import numpy as np
import requests
import json

url = "http://192.168.1.105:5555/similarity"

groupKeyword =["プライバシー","セキュリティ","メディア"]

keyword = [
    ["秘密","非公開","インフォーマル"], #0  類語
    ["個人情報保護","権利","匿名"],  #1　Wiki
    ["個人","氏名","生年月日"], #2  個人情報保護法
    ["安全","警備","保障"], #3　　類語
    ["危険","脅威","コンピュータセキュリティ"],  #4　Wiki
    ["脆弱性","パスワード","暗号"], #5　IPA
    ["手段","媒体","情報"],  #6　　類語
    ["媒体","伝送路","マスメディア"], #7  Wiki
    ["新聞","出版","放送"] #8  マスメディア
]
len_u = len(keyword)  #9
len_k = len(keyword[0])  #3
len_g = len(groupKeyword)

sim=[]
for i in range(len_u):
    sim_g = []
    for j in range(len_g):
        sim_kw = []
        for kw in keyword[i]:
            data = {"word1":groupKeyword[j], "word2":kw}
            jsonData = requests.get(url, params=data).json()
            sim_kw.append(round(jsonData["similarity"],3))
        #print(sim_kw)
        sim_g.append(sim_kw)
    print(sim_g)
    sim.append(sim_g)
#print(sim)

len_i = len(sim)      # 7
len_j = len(sim[0])   # 3

gkey=[[] for j in range(len_j)]
similarity_max = [[ 0 for i in range(len_j)] for j in range(len_i)]  #初期化

for i in range(len_i):
    for j in range(len_j):
        similarity_max[i][j]=max(sim[i][j])
    print(similarity_max[i])

# numpy により最大値をとる行と列の座標を返す
for i in range(len_j):
    for k in range(len_i):
        nps = np.array(similarity_max)
        u,s = np.unravel_index(np.argmax(nps), nps.shape)
        # u: 行(縦方向)座標
        # s: 列(横方法)座標
        gkey[s].append(u)
        # 最大値の座標を削除することはできないので、-1にセットする。
        similarity_max[u][s]=-1
    print(gkey)

# gkey グループキーワードに対して、ユーザを高いSimilarity順にならべた配列
len_g = len(gkey)      # 3  行数：教員のグループキーワード数
len_u = len(gkey[0])   # 7　列数：Similarityの高いユーザID順

group=[[] for i in range(len_g)]  #初期化

for j in range(len_u):  #ユーザ数分繰り返し
    i = j % len_g       #余りによりグループを決定
    top = gkey[i][0]    #左側=Similarityの高い順からユーザを取出
    group[i].append(top)    #教員のグループキーワードにユーザをアサイン
    for k in range(len_g):  #それぞれのグループキーワードを対象
        gkey[k].remove(top)  #アサインしたユーザをすべて削除

print(group)  #グループキーワードへのアサイン結果
#print(gkey)   #すべてがアサインされると空リストとなる

