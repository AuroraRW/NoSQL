# Question
Introduction  
CouchDB is a popular document-type database. Since it uses the http protocol and JSON for
communications, libraries are easy to create for various programming environments. In this assignment,
you will use Python to demonstrate access to a CouchDB database. You will be implementing a simple
contact list.  
Requirements  
Please implement a solution to address the following requirements using Python and CouchDB:  
1. As the Python program starts, the user is asked for  
   a. The CouchDB URI  
   b. The CouchDB administrator id  
   c. The CouchDB administrator password  
   d. The Database to use for the Contact system.
2. The information in the previous requirement is used to connect to the server and check if the
database exists. If the database does not exist, then it should be created.  
3. The data that must be stored for each contact is as follows:  
   a. First name (required)  
   b. Last name (required)  
   c. Email address (required)  
   d. Phone number (optional)  
   e. Notes (optional)
4. The main part of the system is menu driven with the following options:  
   1. List all contacts  
   2. Enter a new contact  
   3. Find a contact  
   4. Delete a contact  
   5. Exit the program  
5. Implement the code for each of the options, using the database you connected to (or created) in
step 2 of the requirements.  
   a. For “Find a contact”, search by last name. You may get more than one result.  
   b. For “Delete a contact”, use the document id. Please ask for confirmation before you
delete.  
6. After an option is executed in the menu, the menu should be shown again to choose another
option. However, option 5. should exit the program.
