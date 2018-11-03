
from flask import jsonify, request
from Src import src
from Menu import menu
from TimeManager import tm, MyTime
from DataManager import dm
import time
import copy


class Manager() :
    def __init(self) :
        None

    def process(self, s, req = None) :
        '''
        friend
        chat_room
        '''
        if s == 'keyboard' :
            # /keyboard 에서 get으로 keybod를 요청하는 경우 user_key를 알 수 없다.
            # 따라서 현재 날짜(tm.mainTIme)의 keybod(default keybod == include ' ')를 반환한다
            return jsonify(self.keybod()), 200
        elif s == 'message' :
            print(req)

            if tm.update() :
                menu.update()
            
            # req['content'] == usually '아침', '점심', '저녁'
            content = req['content']
            user_key = req['user_key']

            # /keyboard get 요청으로 생성된 keybod에는 현재 날짜의 button이 활성화 되므로
            # userTime이 아닌 현재 날짜(tm.mainTIme)의 메뉴를 보내줘야한다.
            # 또한 userTime을 현재 날짜(tm.mainTIme)으로 set해줘야 한다.
            if '　' in content : # '　' == '\u3000'
                dm.setUserTime(user_key, tm.mainTime)
                content = content[:-1]
            if content[:2] == '아침' :
                content = '아침'

            # response
            resp = dict()

            # 아침 점심 저녁
            if content in src.mealTime :
                resp['message'] = {'text' : menu.getMeal(content, dm.getUserTime(user_key))}
            # '이전 날로 날짜 변경'
            elif content == src.keybod['buttons'][3] :
                userTime = dm.getUserTime(user_key)
                userTime = MyTime(userTime.sec - 86400)
                dm.setUserTime(user_key, userTime)
                resp['message'] = {'text' : '날짜 변경 - ' + userTime.toString()}
            # '다음 날로 날짜 변경'
            elif content == src.keybod['buttons'][4] :
                userTime = dm.getUserTime(user_key)
                userTime = MyTime(userTime.sec + 86400)
                dm.setUserTime(user_key, userTime)
                resp['message'] = {'text' : '날짜 변경 - ' + userTime.toString()}
            else :
                resp['message'] = {'text' : '아직 구현되지 않은 기능입니다....\n' + \
                                            '사용에 불편을 드려 죄송합니다 ㅠㅠ'}
            
            resp['keyboard'] = self.keybod(user_key)
            return jsonify(resp), 200
        elif s == 'addFriend' :
            dm.addUser(req['user_key'])
            return '', 200
        elif s == 'removeFriend' or s == 'exitChatRoom':
            dm.removeUser(req)
            return '', 200
        else :
            return jsonify(self.keybod()), 200

    # keybod = {'type' : 'buttons', 'buttons' : self.mealTime + ...}
    # type(structTime) == time.struct_time == type(tm.mainTime.st)
    # when call keybod function, must jsonify return value
    # default == True : /keyboard get -> tm.mainTime keybod
    def keybod(self, user_key = None) :
        tm.update()        
        keybod = copy.deepcopy(src.keybod)

        if user_key == None :
            myTime = tm.mainTime
            keybod['buttons'].pop(3)
        else :
            myTime = dm.getUserTime(user_key)
            if myTime == tm.mainTime :
                keybod['buttons'].pop(3)
        
        keybod['buttons'][0] += ' - ' + myTime.toString()
        if user_key == None :
            whiteSpace = '　' # whiteSpace == '\u3000'
            for i in range(len(keybod['buttons'])) :
                keybod['buttons'][i] += whiteSpace
        return keybod

manager = Manager()
