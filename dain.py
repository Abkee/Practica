import urllib
import requests
from bs4 import BeautifulSoup
import sys

glo_site = []
mas = []
mastwo = []

cheked  = []

def func(url, word, deep):
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page, features='lxml')
    d = 1
    # проверка главную страницу
    if word in soup.text:
        print(f'слова  {word} найдена на странице {url} на глубине {d}')
        return

    for link in soup.findAll('a'):
        tag = link.get('href')
        if tag is not None and 'http' in tag:
            mas.append(tag)
    mass = mas
    d = d + 1
    while (True):
        if d > deep:
            print('Не удалось найти слова в заданном глубине')
            break
        if cheak(mass, word) == True:
            print(f'Слова {word} найдено на глубине {d} ,  на сайте {glo_site}')
            break
        mass = work(mass)
        d = d + 1

# переход к +1 глубине
def work(mas):
    mastwo.clear()
    for i in mas:
        html_page = urllib.request.urlopen(i)
        soup = BeautifulSoup(html_page, features='lxml')
        for link in soup.findAll('a'):
            tag = link.get('href')
            if tag is not None and str(tag).startswith('http'):
                if tag not in mas and tag not in cheked:
                    mastwo.append(tag)
    return mastwo


# Проверка массива
def cheak(mas, word):
    for i in mas:
        html_page = urllib.request.urlopen(i)
        soup = BeautifulSoup(html_page, features='lxml')
        text = soup.text
        # print(text)
        if word in text:
            glo_site.append(i)
            return True
        else:
            cheked.append(i)
    return False



if __name__ == '__main__':
    if len(sys.argv) == 4:
        url = sys.argv[1]
        print("url = ", url)
        word = sys.argv[2]
        print("word = ", word)
        deep = int(sys.argv[3])
        if deep<1:
            print("Глубина не может быть меньше 1")
        elif deep>5:
            print("Глубина не может быть больше 5")
        else:
            func(url, word, deep)