# Question
MongoDB is considered the most popular document-type NoSQL database. It has great community
support and offers access on many platforms using many programming environments.
In this exercise, you will utilize Mongo Atlas and Python to do some processing.   
Requirements  
Please implement a solution to address the following requirements using Python and MongoAtlas:  
1. Set up the free account for MongoDB Atlas on any one of the three cloud platforms.  
2. Create an admin account for the Cluster for the instructor   
3. Create a database called BDSA-06 in your cluster  
4. Using the files people.json and movies.json provided, create the
collections - movies and people - in the BDSA-06 database.  
5. Process the data to create a new collection called fullmovies. This new collection will contain all the documents in the
movies collection, and a new field called cast, with an array of the cast data
This is to be done with a Python program that iterates through the two collections (movies and
people) and writes to the third (fullmovies). Please ask for the instructor’s userid and password
at the start of the program, and use those credentials to access the MongoDB Atlas database.  
6. Write one Python program with a menu system, or several individual Python programs, to do
the following, using ONLY the fullmovies collection. Please ask for the instructor’s userid and
password at the start of the program, and use those credentials to access the MongoDB Atlas
database.  
  a. List all movie titles with only the names of the cast members. (Create an index for this.)  
  b. Ask for a cast member, and display all movies that the member is in. (Create an index for
this.)  
c. Ask for a keyword, and search the “overview” field to return the title and overview for
each match. (Create an index for this.)
