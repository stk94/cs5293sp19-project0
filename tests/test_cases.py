import pytest

import urllib.request
#from bs4 import BeautifulSoup
import tempfile
import PyPDF2
from PyPDF2 import PdfFileReader
import re
import sqlite3



import project0
from project0 import project0


url = "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-16%20Daily%20Arrest%20Summary.pdf"

def test_fetch_incidents():
    assert project0.fetchincidents(url) is not None


def test_download_size():
    assert len(project0.fetchincidents(url)) == 30829

def test_page1_size():
    text = project0.fetchincidents(url)
    fp = tempfile.TemporaryFile()
    fp.write(text)
    fp.seek(0)

    # Read the PDF
    pdfReader = PdfFileReader(fp)
    pdfReader.getNumPages()

    # Get the first page
    page1 = pdfReader.getPage(0).extractText()

    assert len(page1) == 2459

def test_count_observations():
    text = project0.fetchincidents(url)
    observations = project0.extractincidents(text)
    assert len(observations) == 14

def test_populate_db():
    text = project0.fetchincidents(url)
    incidents = project0.extractincidents(text)
    project0.createdb()
    conn = sqlite3.connect('normanpd.db')
    c = conn.cursor()
    No_of_obs = len(incidents)
    for i in range(0, No_of_obs - 1):
        c.execute("INSERT INTO arrests VALUES(?,?,?,?,?,?,?,?,?)",(incidents[i][0],incidents[i][1],incidents[i][2],incidents[i][3],incidents[i][4],incidents[i][5],incidents[i][6],incidents[i][7],incidents[i][8]))
        conn.commit()

    c.execute('SELECT COUNT(case_number)FROM arrests;')
    obs_populated = c.fetchone()
    obs_populated = obs_populated[0]
    assert obs_populated == 13




