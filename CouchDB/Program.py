#####################################################################
##  This script is a program of couchDB including the function of  ##
##  list, search, insert and delete.                               ##
##  Aurora                                                         ##
#####################################################################

import couchdb

#Connect Server and database, 
#if database doesnot exist, create it

def ConnectDB_RW():
    URI_RW=input("Enter URI:")
    ID_RW=input("Enter ID:")
    PW_RW=input("Enter password:")
    dbname_RW=input("Enter database for test:")

    couch = couchdb.Server(URI_RW)
    couch.resource.credentials=(ID_RW,PW_RW)

    #If database exists, then delete and create a new one, 
    #If database does not exists, create it
    if dbname_RW in couch:
        db_RW=couch[dbname_RW]
    else:
        db_RW=couch.create(dbname_RW)
              
    return db_RW

#The menu
def Menu_RW():
    print('\n')
    print("The Menu:")
    print("1.List all contacts")
    print("2.Enter a new contact")
    print("3.Find a contact")
    print("4.Delete a contact")
    print("5.Exit the program")
    result_RW=input("Please input one option:")
    print('\n')
    return result_RW

#List contacts
def List_RW(db_RW):
    print('All contacts are:')
    mango_RW = {'selector': {}, 'fields': ['_id','Firstname',
                                            'Lastname','Emailaddress','phonenumber','notes']}
    for row_RW in db_RW.find(mango_RW):
        print('The id is:',row_RW['_id'])
        print('The First name is:',row_RW['Firstname'])
        print('The Last name is:',row_RW['Lastname'])
        print('The Email address is:',row_RW['Emailaddress'])      
        print('The phone number is:',row_RW['phonenumber'])
        print('The notes is:',row_RW['notes'])
    return

#Insert contact
def Instert_RW(db_RW):
    P_RW=''
    N_RW=''
    DOCID_RW=input("Enter ID of Contact:")
    FN_RW=input("Enter First name:")
    LN_RW=input("Enter Last name:")
    EM_RW=input("Enter Email address:")
    P_YN_RW=input("Do you want to enter a phone number?y/n")
    if P_YN_RW=='y':
          P_RW=input("Enter phone number:")
    N_YN_RW=input("Do you want to enter a notes?y/n")
    if N_YN_RW=='y':
        N_RW=input("Enter Notes:")
    try:            
        doc={
            '_id': DOCID_RW,
            'Firstname':FN_RW,
            'Lastname' :LN_RW,
            'Emailaddress':EM_RW,
            'phonenumber':P_RW,
            'notes':N_RW
            }
        db_RW.save(doc)
        print('Insert sucessfully!')
    except:
        print('Insert unsucessfully')
    
    return

#Search contact
def Search_RW(db_RW):
    LN_RW=input("Enter the Last name to search:")
    mango_RW = {'selector': {}, 'fields': ['_id','Firstname',
                                            'Lastname','Emailaddress','phonenumber','notes']}
            
    for row_RW in db_RW.find(mango_RW):
        try:
            if row_RW['Lastname']==LN_RW:
                print('The id is:',row_RW['_id'])
                print('The First name is:',row_RW['Firstname'])
                print('The Last name is:',row_RW['Lastname'])
                print('The Email address is:',row_RW['Emailaddress'])      
                print('The phone number is:',row_RW['phonenumber'])
                print('The notes is:',row_RW['notes'])
        except:
            print('Search unsucessfully!')
            
    return

#Delete contact
def Delete_RW(db_RW):
    D_RW=input("Enter the ID to delete:")
    D_YN_RE=input("Do you want to delete?y/n")
    if D_YN_RE=='y': 
        try:
            doc=db_RW[D_RW]
        except:
            print('Not found this item!')
        try:
            db_RW.delete(doc)                  
            print('Delete Done!')
        except:
            print('Delete unsuccessfully!')        
    return

#The operation of list, insert, search and delete
def Function_RW():
    db_RW=ConnectDB_RW()
    result_RW=Menu_RW()
    while True:
        #list all contact
        if result_RW=='1':  
            List_RW(db_RW)
            #list menu again    
            result_RW=Menu_RW()  
        
        #insert contact into database
        elif result_RW=='2':
            Instert_RW(db_RW)
            #list menu again
            result_RW=Menu_RW()
            
        #search by last name
        elif result_RW=='3':
            Search_RW(db_RW)  
            #list menu again
            result_RW=Menu_RW()
            
        #delete by ID
        elif result_RW=='4':
            Delete_RW(db_RW)
            #list menu again
            result_RW=Menu_RW()
            
        #stop program    
        elif result_RW=='5':            
            break
    return

#In main, run the function of the system
if __name__=='__main__':
    Function_RW()
