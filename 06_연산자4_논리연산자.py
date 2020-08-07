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

'''
# 1. and 논리값
print( True and True ) #  True
print( True and False ) #  False
print( False and True ) #  False
print( False and False ) #  False

n = 10
n2 = 5
# 질문:  n이 10보다 크고 n2는 5와 같냐?
print( n>10 and n2==5)
print()
# 2. or 논리값
print( True or True ) #  True
print( True or False ) #  True
print( False or True ) #  True
print( False or False ) #  False
x = 10
y = 20
# 질문:  x값이 y값보다 작거나 x값이 짝수냐?
print(x<y  or  x%2==0)
# 3. not
print(not True)
print(not False)