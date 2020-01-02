# Question  
Cassandra is a NoSQL database classified as a Column-type data store. In this exercise, you will build a
database and conduct queries using the DVD scenario. In order to create the appropriate database, 
please review all the requirements before you design the table.  
Requirements  
Please implement a solution to address the following requirements using Cassandra. You will be
required to submit all the code used to create the Keyspace, table(s), any indexes, data inserts and
queries in a single script file.  
1. The Keyspace should be called DVDxxx.  
2. The table should be called DVDTablexxx. If you need more than 1 table, 
use a descriptive name of your choice.  
3. If you need to create one or more indexes, please use the format idx_columnname where
columnname is the name of the column being indexed.  
4. Each record of a DVD must contain:  
   a. The DVD title  
   b. A list of actors in the movie (can be more than 1)  
   c. Cost of the DVD  
   d. DVD genre 
   e. DVD release date  
5. Create test data to demonstrate each of the requirements In 6., below.  
6. Create a query for each of the following required results. DO NOT user the ALLOW FILTERING
clause in the SELECT statements:  
   a. All DVD titles, prices and genres  
   b. All DVD titles and prices sorted by price in descending order for a specific genre (of your
choice).  
   c. DVD titles and prices for the genre ‘Animation’  
   d. The count of the number of unique genres represented in the database.  
   e. The average price of DVD’s in each genre.  
   f. The list of all DVD titles with all the actors’ names for each title.  
   g. The list of DVD titles that any one actor stars in. (You can choose the actor name, but
pick one that has is in more than one movie.  
   h. The list of DVD titles and their release dates, where the release date is in the year 2000.  
   i. The list of DVD titles and their release dates, where the release date is in the year 2000.  
