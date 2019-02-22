# -*- coding: utf-8 -*-
# Example main.py
import argparse

import urllib
#from bs4 import BeautifulSoup
import tempfile
import PyPDF2
from PyPDF2 import PdfFileReader
import re
import sqlite3
import project0

def main(url):
    # Download data
    data_raw = project0.fetchincidents(url)

    # Extract Data
    incidents = project0.extractincidents(data_raw)
	
    # Create Dataase
    project0.createdb()
	
    # Insert Data
    project0.populatedb(incidents)
	
    # Print Status
    project0.status()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--arrests", type=str, required=True, 
                         help="The arrest summary url.")
     
    args = parser.parse_args()
    if args.arrests:
        main(args.arrests)
