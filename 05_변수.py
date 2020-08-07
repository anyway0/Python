'''
  변수(variable)
  1) 용도: 데이터 저장
  2) 문법:
      변수명 = 데이터값
'''
name = "홍길동"
age = 20
weight = 74.63
isMarried = True
email=["aaa@daum.net", "bbb@naver.com"]
phones={"011","013"}
pets={
    "cat":"야옹이",
    "dog":"멍멍이"
}
print("이름:{0}".format(name))
print("나이:{0}".format(age))
print("체중:{0:2f}".format(weight))
print("email:{0}".format(email))
print("phones:{0}".format(phones))
print("pets:{0}".format(pets))


