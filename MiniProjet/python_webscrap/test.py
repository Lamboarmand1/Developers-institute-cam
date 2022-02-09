from bs4 import BeautifulSoup
import requests

url  = requests.get('https://www.cameroondesks.com/search/label/scholarship?&max-results=6').text
soup = BeautifulSoup(url, 'lxml')
#print(soup)

bourses = soup.find_all('div', class_ = "date-outer")
f  = open('fichier.txt', 'a')
for bourse in bourses:
    bourse_name = bourse.find('h2', class_= "post-title entry-title").find('a').text
    bourse_date = bourse.find('h2', class_= "date-header").find('span').text
    print(bourse_name  + 'publié le ' + bourse_date)
    texte = bourse_name  + 'publié le ' + bourse_date
    f.write('\n '  + texte )
