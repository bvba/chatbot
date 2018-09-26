
from Parsing import parsing
import time

class Menu :
	def __init__(self) :
		# date를 이용하여 식단 정보가 최신 상태인지 확인
		self.__date = []
		# 식단 정보
		self.__meal = dict()
		# 식단 정보를 갱신
		self.__update()

	def getMeal(self, content) :
		self.__update()
		return self.__meal[content]

	def __update(self) :
		if self.__date == list(time.localtime())[:3] :
			return
		self.__date = list(time.localtime())[:3]
		self.__meal = parsing.getData()
        
menu = Menu()
