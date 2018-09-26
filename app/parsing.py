
from bs4 import BeautifulSoup
import src
import urllib.request


class Parsing :
	def __init__(self) :
		self.__url = 'https://coop.koreatech.ac.kr:45578/dining/menu.php'
		self.__data = dict()
		self.__parsing()

	def getData(self) :
		return self.__data

	def __parsing(self) :
		with urllib.request.urlopen(self.__url) as fs :
			soup = BeautifulSoup(fs.read()
								.decode('euc-kr')
								.replace('timeo', 'time')
								.replace('listo', 'list')
								.replace('\r', '')
								.replace('\t', '')
								.replace('kcal', 'kcal\n')
								, 'html.parser')
			items = soup.find_all('td', {'class' : 'menu-list'})

		for i in range(3) :
			tmpData = ''
			for j in range(5) :
				txt = items[i * 8 + j].get_text()
				if txt == '\n\xa0\n' : continue
				tmpData += ('# ' + src.mealMenu[j] + txt + '─' * 12 + '\n')
			self.__data[src.mealTime[i]] = tmpData[:-2]