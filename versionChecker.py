import requests
from bs4 import BeautifulSoup

# NOT WORKING!!!!!

VERSION = '1.2'
GIT = "https://github.com/ANTIoffz/FoodParcer/blob/master/foodparcer.py"
HUNDLERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0(iPad;CPU OS 110like Mac OSX)AppleWebKit/604.1.34(KHTML,like Gecko)Version/11.0 Mobile/15A5341f Safari/604.1"
}




def checkVersion():
    print('Проверка обновлений...')
    print(f'Текущая версия: {VERSION}')

    req = requests.get(GIT, headers=HUNDLERS)
    src = req.text
    soup = BeautifulSoup(src, "xml")
    with open('html.html', 'w', encoding='utf-8') as file:
        file.write(src)
    # lastVersion = soup.find('a', class_='commit-author user-mention').find('a', class_='Link--primary markdown-title').text
    # print(f'Последняя версия: {lastVersion}')
checkVersion()