# 学生KeywordとグループKeywordのSimilarity Matrixが得られたとした各種Try & Error

import numpy as np

# [[group keyword#1],[group keyword#2],[group keyword#3]]
user = [
[[0.54,0.72,0.44],[0.02,0.52,0.63],[0.41,0.01,0.61]],
[[0.31,0.55,0.66],[0.22,0.42,0.87],[0.48,0.74,0.87]],
[[0.22,0.33,0.52],[0.21,0.33,0.41],[0.24,0.34,0.23]],
[[0.65,0.10,0.21],[0.66,0.72,0.13],[0.76,0.87,0.12]],
[[0.81,0.05,0.69],[0.55,0.29,0.18],[0.80,0.65,0.53]],
[[0.13,0.87,0.63],[0.87,0.49,0.39],[0.90,0.29,0.64]],
[[0.56,0.02,0.32],[0.17,0.34,0.54],[0.22,0.40,0.32]]
]

# ユーザ行の削除
# print("*** user ***")
# print(user)
# print("*** user pop ***")
# print(user.pop(2))
# print(user)

gnumber = 3

len_i = len(user)      # 7
len_j = len(user[0])   # 3
#print(len_i,len_j)
# group = [0 for i in range(gnumber)]

q = len_i // gnumber  #2
r = len_i % gnumber   #1  1グループは3ユーザ

#print(max_member)

similarity_max = [[ 0 for i in range(len_j)] for j in range(len_i)]  #初期化

for i in range(len_i):
    for j in range(len_j):
        similarity_max[i][j]=max(user[i][j])

# numpy により行と列の座標を返す
for k in range(len_i):
    nps = np.array(similarity_max)
    u,s = np.unravel_index(np.argmax(nps), nps.shape)
    print(u,s)
    print(similarity_max)
    similarity_max[u] = [ -1 for i in range(len_j)]

