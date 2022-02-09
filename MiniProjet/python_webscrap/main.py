from  bs4 import BeautifulSoup
with open('home.html', 'r') as fic:
    content = fic.read()
    #print(content)
    soup = BeautifulSoup(content, 'lxml')
    links = soup.find_all('a')
    print(links)
    f  = open('fichier.txt', 'a')
    
    for link in links:
        print(link.text)
        f.write('\n '  + link.text )
    #print(soup.prettify())
   # print(soup.find('p', class_="lead").string)
    
    