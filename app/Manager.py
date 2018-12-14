
from flask import jsonify, request
from Src import src
from Menu import menu
from TimeManager import tm, MyTime
from DataManager import dm
import time
import copy


class Manager() :
    def __init__(self) :
        # TODO
        # 18:31분에 자동으로 menu update
        None

    def process(self, s, req = None) :
        if s == 'keyboard' :
            # /keyboard 에서 get으로 keybod를 요청하는 경우 user_key를 알 수 없다.
            # 따라서 현재 날짜(tm.mainTIme)의 keybod(default keybod == include ' ')를 반환한다
            return jsonify(self.keybod()), 200
        elif s == 'message' :            
            # req['content'] == usually '아침', '점심', '저녁'
            content = req['content']
            user_key = req['user_key']

            if tm.update() :
                menu.update()

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
            # '소개'
            elif content == src.keybod['buttons'][5] :
                resp['message'] = {'text' : src.intro,
                                   'message_button' : {'label' : '문의하기',
                                                       'url' : src.openchatLink}
                                   }
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
    # user_key == None : /keyboard get -> tm.mainTime keybod
    def keybod(self, user_key = None) :
        keybod = copy.deepcopy(src.keybod)

        # /keyboard get 요청
        if user_key == None :
            myTime = tm.mainTime
            keybod['buttons'][0] += ' - 자동'
        # /message post 요청(날짜 변경)
        else :
            myTime = dm.getUserTime(user_key)
            keybod['buttons'][0] += ' - ' + myTime.toString()
            if myTime >= MyTime(tm.mainTime.sec + (menu.getMealSize() - 1) * 86400) :
                # 다음 날로 날짜 변경 버튼 pop
                keybod['buttons'].pop(4)
        
        # /keyboard get 요청시 모든 버튼 뒤에 공백(특수문자)를 넣어줌
        # process 부분에서는 어떤 keybod(keyboard get, message post)에서
        # 버튼을 눌렀는지 모르기 때문
        if user_key == None :
            whiteSpace = '　' # whiteSpace == '\u3000'
            for i in range(len(keybod['buttons'])) :
                keybod['buttons'][i] += whiteSpace
        return keybod

manager = Manager()
