# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import pprint

def main():
    # CSVファイルを取得
#     data = pd.read_csv("data1.csv")
    data = pd.read_csv("data_w2v.csv")  #Word2Vecで生成されたsimilarity データを用いてグルーピング 5,4,2 のグループ
    # Pandasデータフレームをnumpy配列に変換
    data2 = np.array([data['x1'].tolist(), data['x2'].tolist(), data['x3'].tolist()], np.int32)
    # numpy配列を転置
    data2 = data2.T
    # k-means法でクラスタ分析（クラスタ数は3）
    result = KMeans(n_clusters=3).fit_predict(data)
    # クラスタ毎のサンプル数を表示
    data['cluster_id'] = result
    print(data['cluster_id'].value_counts())
    pprint.pprint(result)
if __name__ == "__main__":
    main()