import urllib.request
import tempfile
import PyPDF2
from PyPDF2 import PdfFileReader
import re
import sqlite3 


def fetchincidents(url):
    #url_1 = href_arrest[2]
    data_raw = urllib.request.urlopen(url).read()
    return data_raw

def extractincidents(data_raw):    
    fp = tempfile.TemporaryFile()

    # Write the pdf data to a temp file
    fp.write(data_raw)

    # Set the curser of the file back to the begining
    fp.seek(0)

    # Read the PDF
    pdfReader = PdfFileReader(fp)
    pdfReader.getNumPages()

    # Get the first page
    page1 = pdfReader.getPage(0).extractText()

    page1 = re.sub(" \n", " ", page1)
    page1 = re.sub("-\n", "- ", page1)
    header_and_data = re.split("\n", page1, 12)

    observations = header_and_data[12]
    observations = re.split(";", observations)
    No_of_obs = len(observations)

    for x in range(0, No_of_obs - 1):
        if x != 0:
            observations[x] = re.sub("\n", "", observations[x], 1)
        observations[x] = observations[x].split('\n')

    for i in range(0, No_of_obs - 1):
        str = ""
        length = len(observations[i])
        for x in range(6, length-2):
            str = str + observations[i][x]
            if x != length-3:
                str = str + " "
        observations[i][6] = str
        observations[i][7] = observations[i][-2]
        observations[i][8] = observations[i][-1]
        for x in range(9, length):
            del observations[i][9]

    return(observations)

def createdb():
    conn = sqlite3.connect('normanpd.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS arrests;')
    c.execute('CREATE TABLE IF NOT EXISTS arrests (arrest_time TEXT, case_number TEXT, arrest_location TEXT, offense TEXT,arrestee_name TEXT, arrestee_birthday TEXT,arrestee_address TEXT,status TEXT,officer TEXT)')
    #print(c.execute('select * from arrests;'))
    c.close()
    conn.close()

def populatedb(incidents):
    conn = sqlite3.connect('normanpd.db')
    c = conn.cursor()
    No_of_obs = len(incidents)
    for i in range(0, No_of_obs - 1):
        c.execute("INSERT INTO arrests VALUES(?,?,?,?,?,?,?,?,?)",(incidents[i][0],incidents[i][1],incidents[i][2],incidents[i][3],incidents[i][4],incidents[i][5],incidents[i][6],incidents[i][7],incidents[i][8]))
        conn.commit()
    c.close()
    conn.close()

def status():
    conn = sqlite3.connect('normanpd.db')
    c = conn.cursor()
    c.execute('SELECT * FROM arrests ORDER BY RANDOM() LIMIT 1;')
    random_observation = c.fetchone()
    c.close()
    conn.close()

    thorn = chr(254)
    str_join = thorn.join(random_observation)
    #str_join = re.sub(" ", ",", str_join, 1)
    #str_join = re.sub(",", thorn, str_join)
    str_join = str_join + ';'
    print(str_join)
