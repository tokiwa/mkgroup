import requests
import json

url = "http://192.168.1.105:5555/similarity"

groupKeyword =["プライバシー","セキュリティ","メディア"]
keyword = [
["秘密","非公開","インフォーマル"], #0
["個人情報保護","権利","匿名"],  #1
["個人","氏名","生年月日"], #2
["安全","警備","保障"], #3
["危険","脅威","コンピュータセキュリティ"],  #4
["手段","媒体","情報"],  #5
["媒体","伝送路","マスメディア"], #6
["新聞","出版","放送"] #7
]
len_u = len(keyword)  #8
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
            sim_kw.append(jsonData["similarity"])
        print(sim_kw)
        sim_g.append(sim_kw)
    print(sim_g)
    sim.append(sim_g)
print(sim)
