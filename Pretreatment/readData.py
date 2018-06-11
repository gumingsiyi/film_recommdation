import Pretreatment.getdata as gd
import pandas as pd
import pymongo
import numpy as np
import time

movies = gd.getAllMovies()

data = pd.read_csv('../sim_mat.csv', header=None)

a = movies[0]['_id']
b = a.__str__()
c = {'id': b}
print(c)

conn = pymongo.MongoClient('localhost', 27017)
db = conn.mydb
sim_mat = db.SimMat

print(type(data[1][1].item()))

for x in range(2220):
    for y in range(2220):
        if (x == y) or (data[x][y] == 0):
            continue
        o = {"x_id": movies[x]['_id'].__str__(),
             "y_id": movies[y]['_id'].__str__(),
             "x_title": movies[x]['title'],
             "y_title": movies[y]['title'],
             "x": x,
             "y": y,
             "value": data[x][y].item()
             }
        print(o)
        sim_mat.insert(o)

print("success")
