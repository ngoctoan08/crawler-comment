from pymongo import *
class MongoDB:
    __connect  = None #private connect
    __mongodb = None #private mongodb
    def __init__(self):
        self.__connect = pymongo.MongoClient("mongodb://localhost:27017/")
        self.__mongodb =  self.__connect["tobaco-crawler-webamin-dev"]
        return __mongodb

    



