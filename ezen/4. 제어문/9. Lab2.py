# 경빈이는 평소 스마트폰을 너무 많이 사용하여 개발 시간을 다 빼앗기고 있었습니다.
# 이렇게 가면 얼마 남지 않는 팀플을 완성하지 못 할 뻔했습니ㅏㄷ.
# 경빈이가 개발시간을 다 채울 경우에만 스마트폰을 사용할 수 있도록 프로그램을 작성하세요.
# 조건) 10시간 이상 : 스마트폰 잠금 해제, 5시간 이상 : 스마트폰 30분 사용 가능, 나머지 : 사용 불가능
# 개발시간을 입력하세요(시간) >>> 10
# 스마트폰 잠금이 해제됩니다.
# 개발시간을 입력하세요(시간) >>> 5
# 30분간 스마트폰 사용이 가능합니다.
# 개발시간을 입력하세요(시간) >>> 2
# 스마트폰 사용이 불가능 합니다.

dev_time = int(input("개발 시간을 입력하세요(시간) >>> "))
if dev_time <= 0 :
    print("잘못된 숫자를 입력하였습니다.")
elif dev_time >= 10 :
    print("스마트폰 잠금이 해제됩니다.")
elif dev_time >= 5 :
    print("30분간 스마트폰 사용이 가능합니다.")
else :
    print("스마트폰 사용이 불가능 합니다.")