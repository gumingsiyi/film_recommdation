import pymongo


def getSet():
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn.mydb
    my_set = db.movies
    return my_set


def getAllMovies():
    data = getSet().find({})
    res = []
    for i in data:
        res.append(i)
    return res


def getAllCasts(data):
    temp = []
    for i in data:
        temp += i['casts']
    res = list(set(temp))
    print(len(res))
    return res


def getAllFeatures(data, cArray, dArray):
    temp = []
    for i in data:
        temp += i['feature']
    res = list(set(temp))
    # 去除只出现过一次的元素
    for i in res:
        temp.remove(i)
    res = list(set(temp))
    # 去除所有演员名字
    for i in cArray:
        if i in res:
            res.remove(i)

    #去除所有导演名字
    for i in dArray:
        if i in res:
            res.remove(i)
    print(len(res))
    return res


def getAllDirectors(data):
    temp = []
    for i in data:
        temp += (i['directors'])
    res = list(set(temp))
    print(len(res))
    return res
