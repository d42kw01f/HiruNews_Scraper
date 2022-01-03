import requests
from bs4 import BeautifulSoup
import os
import re
import lxml

def scraper():
    url = f'https://www.hirunews.lk/local-news.php?pageID={pageNum}'
    header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
    r_main = requests.get(url, headers=header)
    if r_main.status_code == 200:
        soup_page = BeautifulSoup(r_main.text, 'lxml')
        for TheListURL in soup_page.find_all('div', class_='column middle'):
            for TheLinks in TheListURL.findAll('a'):
                theURL = TheLinks.get('href')
                uniqNum = theURL.split('/')[3]
                print(theURL.split('/')[4])
                r = requests.get(theURL, headers=header)
                theSoup = BeautifulSoup(r.text, 'lxml')
                theBody = theSoup.find('div', id='article-phara')
                theRealBodyText = theBody.text.strip()
                print(theRealBodyText)
                with open(f'HiruNewsAriticals/HiruNews_{uniqNum}.txt', 'w', encoding="utf-8") as file:
                    file.write(theRealBodyText)

def main():
    NumPages = int(input('Enter Number of Pages want scrape: '))
