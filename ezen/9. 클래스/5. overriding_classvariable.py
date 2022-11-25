'''
    상속의 업그레이드
        - 클래스 변수 (인스턴스들이 모두 공유하는 변수 )

        - 예
            드래곤 클래스에 인스턴스 속성 추가하기
            부모 클래스에 클래스변수 추가하기
'''

import random

#부모 클래스
class Monster :
    #클래스 변수
    max_num = 1000      # 객체 최대 개수 1000

    #인스턴스 속성
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1    # 객체 생성마다 -1

    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스1
class Wolf(Monster):
    pass

# 자식 클래스2
class Shark(Monster):
    def move(self):     # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("불뿜기", "꼬리치기", "날개치기")

    def move(self):      # 메서드 오버라이딩
        print(f"[{self.name}] 날기")

    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0,2)]}")

wolf = Wolf("울프", 1500, 200)
wolf.move()
print(wolf.max_num)

shark = Shark("상어", 3000, 400)
shark.move()
print(shark.max_num)

dragon = Dragon("드레곤", 8000, 800)
shark.move()
dragon.skill()
print(dragon.max_num)