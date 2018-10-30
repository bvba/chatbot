
from flask import jsonify, request
from Src import src
from Menu import menu
from TimeManager import tm


class Manager() :
    def __init(self) :
        None

    def process(self, url, req = None) :
        '''
        friend
        chat_room
        '''
        if url == 'keyboard' :
            return self.keyboard(), 200
        elif url == 'message' :
            print(req)
            # req['content'] == usually '아침', '점심', '저녁'
            content = req['content']
            if content[:2] == '아침' :
                content = '아침'

            # response
            resp = dict()
            resp['keyboard'] = self.keyboard()

            if content in src.mealTime :
                resp['message'] = {'text' : menu.getMeal(content)}
            else :
                resp['message'] = {'text' : 'error'}
            return jsonify(resp), 200

    def keyboard(self, myTime = tm.mainTime) :
        wday = ['월', '화', '수', '목', '금', '토', '일']
        keybod = src.keybod.copy()
        keybod['buttons'][0] = ('아침 - ' + str(myTime.st[1]) + '.' + str(myTime.st[2]) + \
                                '(' + str(wday[myTime.st[6]]) + ')')
        return keybod

manager = Manager()
