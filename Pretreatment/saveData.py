import Pretreatment.getdata as gd
import pandas as pd
import csv
import numpy as np


def getCasts(data):
    casts = gd.getAllCasts(data)
    data = pd.DataFrame(data=casts)
    data.to_csv("../casts.csv", index=False, header=False)
    return casts


def getDirectors(data):
    directors = gd.getAllDirectors(data)
    data = pd.DataFrame(data=directors)
    data.to_csv("../directors.csv", index=False, header=False)
    return directors


def getFeatures(data, cArray, dArray):
    features = gd.getAllFeatures(data, cArray, dArray)
    data = pd.DataFrame(data=features)
    data.to_csv("../features.csv", index=False, header=False)


movies = gd.getAllMovies()
c = getCasts(movies)
d = getDirectors(movies)
getFeatures(movies, c, d)
