'''
  문자열
  1. 생성방법 4가지
  2. 특징: immutable(변경불가)
  3. 인덱싱과 슬라이싱
  4. 함수
'''
## 1. 문자열생성
#2. 인덱싱과 슬라이싱
m = "sequence"
print("0번째 값:", m[0])
print("1번째 값:", m[1])
print("끝 값:", m[-1])
print("뒤에서 두번째 값:", m[-2])
print()
print("2. 슬라이싱")
print("0부터 3까지:", m[0:4]) #sequ
print("0부터 3까지:", m[:4]) #sequ
print("1부터 끝까지:", m[1:8]) #equence
print("1부터 끝까지:", m[1:]) #equence
print("0부터 끝까지:", m[:]) #sequence
print()
print("0부터 끝까지 2step:", m[::2]) #sqec
print()
print("-3부터 -1전까지 출력:", m[-3:-1]) # nc
print("역순:", m[::-1])






