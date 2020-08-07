'''
  반복문(loop)
  가. for문
     문법:
          for 변수 in 집합형:
              문장
    * 집합형을 자동으로 생성한는 함수
     -range(n):  0~n-1까지 [0,1,....8]
     -range(start,end):  end는 전까지
       예> range(1,5)==> [1,2,3,4]
     -range(start,end,step):
     예> range(1,10,2)==> [1,3,5,7,9]
  나. while문
'''
# 질문: "hello" 10번출력?
# for n in [1,2,3,4,5,6,7,8,9,10]:
#     print("hello")
for n in range(10):
    print("hello", n)
print()
for n in range(1,5):
    print("world", n)
print()
for n in range(1,10,2):
    print("happy", n)
help(range)
