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
'''
n = 10
n2 = 3
print("더하기:{}".format(10+3))
print("빼기:{}".format(10-3))
print("곱하기:{}".format(10*3))
print("나누기:{}".format(10/3)) # 3.3333333333333335
print("몫:{}".format(10//3)) # 3
print("나머지:{}".format(10%3)) # 1
print("제곱:{}".format(10**3)) # 1000

#몫과 나머지 함께 구하기: divmod(10,3)
result = divmod(10,3)
print("몫과 나머지:{}".format(result)) # (3,1)
a, b = divmod(10,3)  # a, b= (3,1)
print("몫:{}, 나머지:{}".format(a,b))
