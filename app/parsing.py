from bs4 import BeautifulSoup
import urllib.request

url = 'https://coop.koreatech.ac.kr:45578/dining/menu.php'

with urllib.request.urlopen(url) as fs :
    soup = BeautifulSoup(fs.read()
                         .decode('euc-kr')
                         .replace('timeo', 'time')
                         .replace('listo', 'list')
                         .replace('\r', '')
                         .replace('\t', '')
                         .replace('kcal', 'kcal\n')
                         , 'html.parser')
    items = soup.find_all('td', {'class' : 'menu-list'})

meal = dict()
sMealTime = ['아침', '점심', '저녁']
sMealMenu = ['한식', '일품', '특식 (전골 / 뚝배기)', '양식', '능수관', '수박여']
for i in range(3) :
    mealList = ''
    for j in range(8) :
        txt = items[i * 8 + j].get_text()
        if txt != '\n\xa0\n' :
            mealList += ('# ' + sMealMenu[j] + '\n' + txt + '-' * 15 + '\n')
    
    meal[sMealTime[i]] = mealList[:-2]
