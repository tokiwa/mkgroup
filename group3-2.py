gkey = [
    [5, 4, 0, 1, 3, 6, 2],   #gkey1 康similarityユーザ順
    [2, 1, 5, 6, 3, 0, 4],   #gkey2
    [6, 5, 1, 3, 4, 0, 2]    #gkey3
]
print(gkey)

len_i = len(gkey)      # 3
len_j = len(gkey[0])   # 7

group=[[] for i in range(len_i)]

print(len_i, len_j)

for i in range(len_i):
    gkey[i].remove(5)
print(gkey)
