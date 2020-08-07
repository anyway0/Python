'''
   연산자
   1. 산술연산자
     +: 더하기
     -: 빼기
     *: 곱하기
     /: 나누기 ( 소수점포함 반환)
     //: 몫
     %: 나머지
     **: 제곱

   2. 대입연산자
   - n += n2 : n= n+n2
   - n -= n2 : n= n-n2
   - n *= n2 : n= n*n2
   - n /= n2 : n= n/n2
   - n //= n2 : n= n//n2
   - n %= n2 : n= n%n2
   
  3. 비교연산자 ==> 실행결과는 True/False
    a == b: a 와 b 가 같냐?
    a != b: a 와 b 가 같지 않냐?
    a > b: a 가 b 보다 크냐?
    a >= b: a 가 b 보다 크거나 같냐?
    a < b: a 가 b 보다 작냐?
    a <= b: a 가 b 보다 작거나 같냐?

   4. 논리 연산자==> 논리값(True/False)이용해서 연산
     가. 논리값 and 논리값 (그리고)
     나. 논리값 or 논리값 ( 또는 )
     다. not 논리값( 부정 )
     
    * True/False가 아닌 임의의 값도 논리값으로 처리한다.(*****)
    ==> 논리값으로 변환하는 함수: bool(값)
'''

#1. False 로 처리하는 임의의 데이터
print("0:", bool(0))
print(" '' :", bool(''))
print(' "":', bool(""))
print('[]:', bool([]))
print('{}:', bool({}), type({}))
print('None:', bool(None))
# 2. 위의 데이터가 아닌 데이터는 모두 True로 처리
print("10:", bool(10))
print(" 'xxx':", bool('xxx'))
print(" 'xxx':", bool("xxx"))
print("[10,20]:", bool([10,20]))

# 활용
kkk = [10]
kkk=''
kkk={}
kkk=None
# 질문: kkk값이 비어있으면 100출력하고 값이 있으면 200출력?
if kkk: # 매우 중요함
    print("100") # 조건식 True인 경우 실행
else:
    print("200") # 조건식 False인 경우 실행