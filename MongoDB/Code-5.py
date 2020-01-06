######################################################################
## This script is for the operation of MongoDB on BDSA-06 database  ##
## Aurora                                                           ##
######################################################################

from pymongo import MongoClient
username=input('Enter a username:')
password=input('Enter a password:')

#connect Mongo Atlas 
client = MongoClient('mongodb://%s:%s@cluster0-shard-00-00-axemk.mongodb.net:27017,cluster0-shard-00-01-axemk.mongodb.net:27017,cluster0-shard-00-02-axemk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'%(username, password))
db = client['BDSA-06']
collection=db['fullmovies']

#copy documents from movies to fullmovies
for docmovies in db['movies'].find({}):
    collection.insert_one(docmovies)

#add field of cast to fullmovies
for docmovies in db['movies'].find({}):
    moviesname=docmovies['_id']
    for docpeople in db['people'].find({'movies':moviesname}):
        collection.update_one({'_id': moviesname}, {'$set': {'cast': docpeople['_id']}})


