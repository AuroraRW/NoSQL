######################################################
##  This script is for adding test data in database ##
##  Aurora                                          ##
######################################################

#Connect Server
import couchdb
URI_RW=input("Enter URI:")
ID_RW=input("Enter ID:")
PW_RW=input("Enter password:")
dbname_RW=input("Enter database for test:")

couch = couchdb.Server(URI_RW)
couch.resource.credentials=(ID_RW,PW_RW)

#If database exists, then delete and create a new one, 
#If database does not exists, create it
if dbname_RW in couch:
    del couch[dbname_RW]
    db_RW=couch.create(dbname_RW)
else:
    db_RW=couch.create(dbname_RW)
    
#Add data into database

doc={
    '_id': '1',
    'Firstname':'Mary',
    'Lastname' :'Lin',
    'Emailaddress':'Mary123@gmail.com',
    'phonenumber':'4356782233',
    'notes':'Mary Lin is a priciple.'
}
db_RW.save(doc)
doc={
    '_id': '2',
    'Firstname':'Lucy',
    'Lastname' :'Zhang',
    'Emailaddress':'Lucy234@163.com',
    'phonenumber':'2335674432',
    'notes':'Lucy Zhang is an english teacher.'
}
db_RW.save(doc)
doc={
    '_id': '3',
    'Firstname':'Lily',
    'Lastname' :'Zhang',
    'Emailaddress':'Lily456@gmail.com',
    'phonenumber':'3456674564',
    'notes':'Lily Zhang is a student.'
}
db_RW.save(doc)
doc={
    '_id': '4',
    'Firstname':'Tom',
    'Lastname' :'Wang',
    'Emailaddress':'T123W@gmail.com',
    'phonenumber':'9987896678',
    'notes':'Tom Wang is a math teacher'
}
db_RW.save(doc)
doc={
    '_id': '5',
    'Firstname':'Jason',
    'Lastname' :'Wang',
    'Emailaddress':'JWtj@163.com',
    'phonenumber':'7898789988',
    'notes':'Jason Wang is a student'
}
db_RW.save(doc)

print("Done!")
