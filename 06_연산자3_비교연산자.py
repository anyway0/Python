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
'''
n = 10
n2 = 3
print( n == n2 )
print( n != n2 )
print( n > n2 )
print( n >= n2 )
print( n < n2 )
print( n <= n2 )

# 비교할 값의 종류
x = [10,20,30]
x2 =[20,30,40]
print("x와 x2의 주소값비교:")
print(x is x2) # id(x) == id(x2) 동일
print("x와 x2의  실제값비교:")
print(x == x2)

# None 비교
xxx = None
print("xxx가 None이냐", xxx is None)
print("xxx가 None이 아니냐", xxx is not None)

