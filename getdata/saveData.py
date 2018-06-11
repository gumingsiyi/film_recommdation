import pymongo
import getdata.getWebsite as web

conn = pymongo.MongoClient('localhost', 27017)
db = conn.mydb
my_set = db.movies


for i in range(99, 200):
    print(i*20)
    start = str(i*20)
    data = web.getMovies(start)
    my_set.insert(data)
