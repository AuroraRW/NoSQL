# Question:
1. Review the three CSV (comma-separated value) files provided.  
   a. You will note that there is a need to use a Serializer/Deserialier to address the issue of
commas in some fields.
2. Write a script to create three tables for the CSV files.  
   a. One table should be called DVDxxx.  
   b. One table should be called Actorxxx.  
   c. One table should be called DVDActorxxx.  
   d. The script files should be called MakeTablesxxx.  
3. Create the tables in Hive by demonstrating the execution of the script.  
4. Import the data from the three CVS files into the three tables.  
   a. Show that the data is actually there with a simple SELECT for each table.  
5. Create one script called Demoxxx to accomplish each of the following required results in Hive.  
   a. All DVD titles, prices and genres  
   b. All DVD titles and prices sorted by price in descending order  
   c. DVD titles and prices for the genre Animation  
   d. All the genres for the DVDs, but only displayed once (not duplicated)  
   e. The count of the number of genres, including the blank genres  
   f. The average price of DVDs for each genre  
   g. The average price of DVDs for each genre, where the average price for that genre is less than (or equal to) $20  
   h. The list of all DVD titles with all the actors’ names for each title (only those DVDs with actors should be listed)  
   i. The list of actor names and their DVD titles, where the actor’s first name or last name contains “john”. (Hint: watch for case sensitivity)  
   j. The list of last names of the actors, with no repeated last names. You can assume the last name is the portion of the actor’s name up to (but not including) the comma.  
   i. Hint: You may need two functions to do this  
   k. The list of DVD titles their release dates, where the release date is in the year 2000.  
   l. Show how many titles are in each genre, but combine Action/Adventure and Action/Comedy into one category called Action. Sort the results in alphabetical order for the genre.  
   i. Hint: You will need to use a Conditional statement.  
6. Demonstrate each of the required results in question 5.  
   a. There will be some long queries. For the lengthy ones (more than 5 seconds in length), to conserve resources, you should pause recording after you start executing the statement, then unpause it when the query finishes.
