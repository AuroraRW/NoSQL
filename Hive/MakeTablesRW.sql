--- Create table DVDRW
create table DVDRW (DVD_Title string, Studio string, Released string, Status string, Sound string, Versions string, Price string, Rating string, Year string, Genre string, Aspect String, UPC String, DVD_ReleaseDate date, ID int,Timestamp timestamp, Updated string)
row format delimited
fields terminated by ','
tblproperties("skip.header.line.count"="1");

--- Create table ActorRW
create table ActorRW (Actor_id int, Actor string)
row format delimited
fields terminated by ','
tblproperties("skip.header.line.count"="1");

--- Create table DVDActorRW
create table DVDActorRW (ID int, Actor_id int, DVDList_id int)
row format delimited
fields terminated by ','
tblproperties("skip.header.line.count"="1");


