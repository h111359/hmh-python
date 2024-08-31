#!/usr/bin/env python

"""
Download the pdfs in a list of links to Springer free books

Usage -

    The script should be placed in a folder and in the same folder
    should be placed a file named "Books_List.txt" where should 
    be placed a list of links to Springer books - one link per row.

    The script should be executed with no arguments and the rdfs will
    be downloaded in subfolder "downloaded"

    If the link leads to a page with no button for pdf download the 
    link will be stored in a file  "skipped_url_list.txt"

Requires - requests >= 2.20.0
           beautifulsoup >= 4.9.0
           pandas >= 0.23.4

Download and install using
    
    pip install requests
    pip install beautifulsoup4
    pip install pandas    
"""

__author__= 'hmhristov <hmhristov@outlook.com>'
__license__= 'MIT'
__version__= '1.0.0'

import requests 
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_pdf_subpage (header_page_url):
    
    page = requests.get(header_page_url)
    soup_header_page = BeautifulSoup(page.text, 'html.parser' )
    current_link = ''
    url = ''
    page_title = soup_header_page.find('h1').text
    for i in (' ', ':', '/', '?', ',', '.', '-', '!', ';'):
        page_title = page_title.replace(i,'')

    book_year=soup_header_page.find('span', class_="bibliographic-information__value", id="copyright-info").text[-4:]

    for link in soup_header_page.find_all('a'):
        current_link = link.get('href')
        title = link.get('title')
        if current_link.endswith('pdf') and str(title) == 'Download this book in PDF format':
            url = 'https://link.springer.com' + current_link
            break  
            
    return (url, book_year + '_Book_' + page_title)

if __name__=='__main__':

    base_dir = os.getcwd()

    bookslist_file_name = base_dir + r"\Books_List.txt"
    print(bookslist_file_name)
    # bookslist_file_name = bookslist_file_name.replace('\\','/')
    
    df_books = pd.read_csv(bookslist_file_name, header=None, names=['Link'])
    check_list_file = open(base_dir + r'\skipped_url_list.txt','a+')

    books_folder = base_dir + r'\downloaded'

    if not os.path.exists(books_folder):
        os.makedirs(books_folder)

    books_folder = books_folder + '\\'

    for my_url in df_books['Link']:

        download_attributes = get_pdf_subpage(my_url)
        url_row = my_url  + '   ' + download_attributes[0] + '    ' + download_attributes[1]

        if download_attributes[0]:
            # The button for PDF download is found
            myfile = requests.get(download_attributes[0])
            print('downloading ' + download_attributes[1])
            open(books_folder  + download_attributes[1] +'.pdf', 'wb').write(myfile.content)  
        else:
            print('Can not download ' + url_row)                    
            check_list_file.write(url_row + '\n')
