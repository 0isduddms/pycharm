# 제어문 - 조건문, 반복문
# ex) 기존 비밀번호 = "0111"
#     입력한 비밀번호 ="0111"
#     만약 비밀번호가 일치하면 --> 로그인 성공!
#     만약 입력을 안했으면 --> 비밀번호를 입력해주세요
#     만약 비밀번호가 일치하지 않으면 --> 로그인 실패!

origin_pw = "0111"
input_pw = input("비밀번호를 입력해주세요 : ")
if input_pw == origin_pw :          # 조건 A
    # 조건 A 참
    print("로그인 성공!")
    print("환영합니다.")
elif input_pw == "" :               # 조건 B
    # 조건 A 거짓, 조건 B 참
    print("비밀번호를 입력해주세요.")
else :
    # 조건 A 거짓, 조건 B 거짓
    print("비밀번호가 일치하지 않습니다.")