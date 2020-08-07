'''
  문자열
  1. 생성방법 4가지
  2. 특징: immutable(변경불가)
  3. 인덱싱과 슬라이싱
  4. 함수
'''
## 1. 문자열생성
#2. 인덱싱과 슬라이싱
#3. 함수 ==> str 관리

# 특정객체의 함수명 알아보기: dir(객체명)
# print(dir(str))
# print(dir(int))
# print(dir(list))
# print(dir(__builtins__))
m = "    sequence   "
print(m.strip())
print(m, len(m)) # 원래문자열은 변경안됨.(immutable)

print("1. 문자열 길이:", len(m))
print("2. 특정 문자의 갯수:", m.count('e'))
print("3. 소문자:", "AbeCex".lower())
print("4. 대문자:", "AbeCex".upper())
print("5. swap:", "AbeCex".swapcase())
print("6. 양쪽공백제거:", "     hello   ".strip())
print("7. 왼쪽공백제거:", "     hello   ".lstrip())
print("8. 오른쪽공백제거:", "     hello   ".rstrip())
print("9. 특정문자양쪽제거:", "HHasdHfasHHH".strip('H'))
print("10. 특정문자왼쪽제거:", "HHasdHfasHHH".lstrip('H'))
print("11 특정문자 오른쪽제거:", "HHasdHfasHHH".rstrip('H'))
print("12 특정문자 변경:", "hello".replace('h','X'))
print("13. 구분자를 활용한 문자열 분리")
m = "aaa/bbb/ccc"
result = m.split("/")
print(result)
print("13 특정문자 시작여부1:", "hello".startswith('h'))
print("13 특정문자 시작여부2:", "hello".startswith('X'))
print("14 특정문자 종료여부1:", "hello".endswith('o'))
print("14 특정문자 종료여부2:", "hello".endswith('X'))
print("15 문자만 구성?:", "hello".isalpha())
print("15 문자만 구성?:", "hello2334".isalpha())
print("15 숫자만 구성?:", "2334".isnumeric())
#실습: 다음문자열에서 숫자(문자)만 뽑으시오
m = "asdasff134asfas094"
print("16 특정문자의 위치값1?:", "hello".find('e'))
print("16 특정문자의 위치값2?:", "hello".find('X')) # 없으면 -1
print("17 특정문자열 포함여부?:", "hello".__contains__('el'))
print("18 특정문자 연결?:", ",".join(['A','B','C']))
print("18 특정문자 연결?:", " 와 ".join(['A','B','C']))
print("19  멤버쉽 연산자:",  'a' in 'abc')
print(dir(str))



