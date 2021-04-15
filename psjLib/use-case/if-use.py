"""
if문에서 참/거짓 으로 활용되는 케이스
참 :
거짓 : None
"""
if_condition = None

if if_condition:
    print("참")
else:
    print("거짓")

"""
배열, 튜플, 문자열에 해당값이 있으면 처리하게..
"""
pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

if 'money' not in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

"""
조건부 표현식 : 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
"""
score = 70
message = "success" if score >= 60 else "failure"
print(message)