'''
  반복문(loop)
  가. for문
     문법:
          for 변수 in 집합형:
              문장
          else:
              문장 (정상종료인 경우에만 실행됨)

    * 집합형을 자동으로 생성한는 함수
     -range(n):  0~n-1까지 [0,1,....8]
     -range(start,end):  end는 전까지
       예> range(1,5)==> [1,2,3,4]
     -range(start,end,step):
     예> range(1,10,2)==> [1,3,5,7,9]

     * 반복문내에서 사용하는 2가지 키워드
     1) break
        ==> 집합형의 갯수만큼 실행되고
        반복문이 종료(정상종료)되는데,
        이전에 반복문을 빠져나올 때(비정상종료).
     2) continue
        ==> 반복해야될 여러문장들중에서
          일부분의 문장들을 skip할 때 사용.

     * else 문
       ==> 정상종료인 경우에만 실행된다.
       
  나. while문
'''
# 1. 정상종료
for n in range(10):
    print(n)
else:
    print("정상종료")
print("end")
print()
# 2. 비정상종료
for n in range(10):
    if n==5:break
    print(n)
else:
    print("정상종료222222222")
print("end2")
print()
print("continue 실습")
for n in range(5):
    print(n)
    if n==3:continue
    print("hello")
    print("world")
else:
    print("정상종료")
print("end")
