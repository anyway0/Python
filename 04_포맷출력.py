'''
 포맷 출력
 예> 이름: 홍길동 나이:20
     이름: 홍길동2 나이:40
     ..
  문법:
      "이름:{0}나이:{1}".format(값, 값2)
'''
print("이름:{} 나이:{}".format("홍길동",20))
print("이름:{0} 나이:{1}".format("홍길동",20))
print("이름:{1} 나이:{0}".format("홍길동",20))
print('{:,}'.format(1234567890))
print('{}'.format(4556.778))
print('{0}'.format(4556.778))
print('{0:.2f}'.format(4556.778))
help('FORMATTING')