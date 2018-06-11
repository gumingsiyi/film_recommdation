import Pretreatment.getdata as gd
import pandas as pd
import numpy as np


# 得到基本数据
movies = gd.getAllMovies()
print(len(movies))

casts = gd.getAllCasts(movies)
directors = gd.getAllDirectors(movies)
feature = gd.getAllFeatures(movies, casts, directors)


# 每部电影的演员阵容矩阵
def dict_casts():
    res = {}
    for i in range(2220):
        m_casts = movies[i]['casts']
        temp = []
        for j in range(4813):
            if casts[j] in m_casts:
                temp.append(1)
            else:
                temp.append(0)
        res[movies[i]['_id']] = temp
    print("成功导入演员")
    return res


def mat_by_casts(dict):
    temp = []
    for movie in dict:
        temp.append(dict[movie])
    ma = np.matrix(temp)
    mb = ma.T
    res = ma*mb
    print(res)
    data = pd.DataFrame(data=res)
    data.to_csv("../casts_mat.csv", index=False, header=False)
    print("生成演员相似度矩阵")
    return res


casts_dict = dict_casts()
cast_mat = mat_by_casts(casts_dict)


# 每部电影的演员阵容矩阵
def dict_directors():
    res = {}
    for i in range(2220):
        m_directors = movies[i]['directors']
        temp = []
        for j in range(1389):
            if directors[j] in m_directors:
                temp.append(1)
            else:
                temp.append(0)
        res[movies[i]['_id']] = temp
    print("成功导入导演")
    return res


def mat_by_directors(dict):
    temp = []
    for movie in dict:
        temp.append(dict[movie])
    ma = np.matrix(temp)
    mb = ma.T
    res = ma*mb
    data = pd.DataFrame(data=res)
    data.to_csv("../directors_mat.csv", index=False, header=False)
    print("生成导演相似度矩阵")
    return res


directors_cast = dict_directors()
dir_mat = mat_by_directors(directors_cast)


# 每部电影的演员阵容矩阵
def dict_features():
    res = {}
    for i in range(2220):
        m_features = movies[i]['feature']
        temp = []
        for j in range(625):
            if feature[j] in m_features:
                temp.append(1)
            else:
                temp.append(0)
        res[movies[i]['_id']] = temp
    print("成功导入特征")
    return res


def mat_by_features(dict):
    temp = []
    for movie in dict:
        temp.append(dict[movie])
    ma = np.matrix(temp)
    mb = ma.T
    res = ma*mb
    data = pd.DataFrame(data=res)
    data.to_csv("../features_mat.csv", index=False, header=False)
    print("生成特征相似度矩阵")
    return res


features_cast = dict_features()
feature_mat = mat_by_features(features_cast)

sim_mat = cast_mat + dir_mat*2 + feature_mat
mat = pd.DataFrame(data=sim_mat)
mat.to_csv("../sim_mat.csv", index=False, header=False)

