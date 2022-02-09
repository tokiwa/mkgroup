# グループKeywordに対する学生ランキングを求めるプログラム

import numpy as np

user = [
[[0.54,0.72,0.44],[0.02,0.52,0.63],[0.41,0.01,0.61]],  #user0
[[0.31,0.55,0.66],[0.22,0.42,0.87],[0.48,0.74,0.87]],  #user1
[[0.22,0.33,0.52],[0.90,0.90,0.41],[0.24,0.34,0.23]],  #user2
[[0.65,0.10,0.21],[0.66,0.72,0.13],[0.76,0.87,0.12]],  #user3
[[0.81,0.05,0.69],[0.55,0.29,0.18],[0.80,0.65,0.53]],  #user4
[[0.13,0.87,0.63],[0.87,0.49,0.39],[0.90,0.29,0.64]],  #user5
[[0.56,0.02,0.32],[0.17,0.77,0.54],[0.93,0.40,0.32]]   #user6
]

len_i = len(user)      # 7
len_j = len(user[0])   # 3

gkey=[[] for j in range(len_j)]
similarity_max = [[ 0 for i in range(len_j)] for j in range(len_i)]  #初期化

for i in range(len_i):
    for j in range(len_j):
        similarity_max[i][j]=max(user[i][j])

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