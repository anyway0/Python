'''
  문장(코드)
  1. 실행문
      가. 순차문
      나. 제어문
         a. 조건문: 단일 if문, if~else문, 다중if문, 3항연산자
         b. 반복문: for문, while 문, ( do~while 지원안됨)

        * 제어문은 :(콜론) 사용해야된다.
         :(콜론)이후의 문장은 반드시 들여쓰기 해야 된다.

  2. 비실행문(주석문)
    - 한줄 주석문: #
    - 여러줄 주석문: triple

'''

# 1. 단일 if문: 조건이 True인 경우에 실행시킬 때 사용.
'''
   문법:
         if 조건식: # 조건식의 형태: 비교연산자,논리연산자,
                   in연산자 + 모든데이터
         
            문장
'''
# 2. if ~ else문: 조건에 따라서 실행문장이 다른경우
'''
 문법:
       if 조건식:
           문장
       else:
           문장
'''
# 3. 다중 if문: 여러번 비교하는 경우
'''
 문법:
       if 조건식:
           문장
       elif 조건식:
            문장
       elif 조건식:
            문장
       ...
       else:
            문장
            
  4. 3항 연산자: if ~ else 문 다른 표현식
  문법:
      변수 =   참  if 조건식 else 거짓
'''
result = 100 if True else 200
print(result)
print()
n = 10
result = "Hello" if n > 20 else 'World'
print(result)


