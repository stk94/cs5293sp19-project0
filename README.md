# cs5293sp19-Project0

Name: SAI TEJA KANNEGANTI
Date: 02/21/2019


Description of the Project:
https://oudalab.github.io/textanalytics/projects/project0


Execution of code: (directions on how to install and use the code)

My code will take a url from the command line and will run the code using the command below.
pipenv run python project0/main.py --arrests <url>
Each run of the above command will create a new normandb database files. 


Approach:

I have done this project in 5 steps. I have written a function for each of the below part.
	1. Download Data
	2. Extract Data
	3. Create Database
	4. Insert Data
	5. Status Print

1. Download Data: Here url of a pdf from Norman police report webpage is given and used urllib.request library to get information in the pdf.

2. Extract Data: Used PyPdf package (PyPdf2.PdfFileReader class)to extract data from pdf file and allows to extract specific pages. Later able to extract observations by seperating with ';'. Later using Regular expressions able to extract each field for every observation.

3. Create Database: Used sqlite3 package to create database called 'normanpd.db'. Created table arrests with given column names.

4. Insert Data: Populated each observation into arrests table.

5. Status Print: Randomly picks a observation and have thorn character seperating each field in an observation and prints it to output. 


Inspiration:
1. https://python.gotrained.com/beautifulsoup-extracting-urls/
2. https://stackoverflow.com/questions/42316425/checking-if-a-word-is-in-a-list-in-python
3. https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python
4. https://www.geeksforgeeks.org/python-string-split/
5. https://www.w3schools.com/python/python_regex.asp
6. http://www.sqlitetutorial.net/sqlite-functions/sqlite-random/
7. https://www.youtube.com/watch?v=o-vsdfCBpsU
8. https://www.youtube.com/watch?v=pd-0G0MigUA&t=1222s
9. https://www.youtube.com/watch?v=IlsikVwUffI
10. http://www.sqlitetutorial.net/sqlite-drop-table/

People contacted:
Chanukya LakshmanSai, chanukyalakamsani@ou.edu, Told me to drop table if it already exists, 2/21/2019
Gowtham Teja Kanneganti, gowthamkanneganti@ou.edu, Discussed about closing db conection in last 3 functions, 2/19/2019

Assumptions:
1. ";" is used as a seperator to seperate two diffrent records of a pdf file.
2. Only " \n" or "-\n" are used as line breakers.
