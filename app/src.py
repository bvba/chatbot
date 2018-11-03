class Src() :
    def __init__(self) :
        self.wday = ['월', '화', '수', '목', '금', '토', '일']
        self.mealTime = ['아침', '점심', '저녁']
        self.mealType = ['한식', '일품', '특식 (전골 / 뚝배기)', '양식', '능수관', '수박여']
        self.keybod = {
            'type' : 'buttons',
            'buttons' : self.mealTime + ['이전 날로 날짜 변경', '다음 날로 날짜 변경']
        }

src = Src()
