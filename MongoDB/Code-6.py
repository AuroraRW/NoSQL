######################################################################
## This script is for the operation of MongoDB on BDSA-06 database  ##
## Aurora                                                           ##
######################################################################

from pymongo import MongoClient
#connect Mongo Atlas
def ConnectMongoDB():
    username=input('Enter a username:')
    password=input('Enter a password:')
    client = MongoClient('mongodb://%s:%s@cluster0-shard-00-00-uklgg.mongodb.net:27017,cluster0-shard-00-01-uklgg.mongodb.net:27017,cluster0-shard-00-02-uklgg.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'%(username, password))
    db = client['BDSA-06']
    collection=db['fullmovies']
    return collection

#List all movies titles with cast numbers
def ListMovies(collection):
    for doc in collection.find({}):
        print(doc['_id'])
        print(doc['cast'])
    return

#List all movies with a specify cast number
def ListMoviesForACast(collection):
    castname=input('Enter a cast name:')
    #castname='Mel Gibson'
    for doc in collection.find({'cast':castname}):
        print(doc['_id'])
    return

#List movies title and overview for keyword
def SearchOverview(collection):
    keyword=input('Enter a keyword for search:')
    #keyword='family'
    for doc in collection.find({'$text':{'$search':keyword}}):
        print(doc['_id'])
        print(doc['overview'])
    return

def Menu():
    print('\n')
    print("The Menu:")
    print("1.List all movies titles with cast numbers")
    print("2.List all movies with a specify cast number")
    print("3.List movies title and overview for keyword")
    print("4.Exit the program")
    result=input("Please input one option:")
    print('\n')
    return result

#The operations
def Function():
    collection=ConnectMongoDB()
    result=Menu()
    while True:
        #List all movies titles with cast numbers
        if result=='1':  
            ListMovies(collection)
            #list menu again    
            result=Menu()  
        
        #List all movies with a specify cast number
        elif result=='2':
            ListMoviesForACast(collection)
            #list menu again
            result=Menu()
            
        #List movies title and overview for keyword
        elif result=='3':
            SearchOverview(collection)  
            #list menu again
            result=Menu()
            
        #Exit the program
        elif result=='4':
            break
            
    return

#In main, run the function of the system
if __name__=='__main__':
    Function()
