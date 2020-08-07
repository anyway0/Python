'''
  변수(variable)
  1) 용도: 데이터 저장
  2) 문법:
      변수명 = 데이터값
  3) 변경가능하기 때문에 변수라고 부른다.
  4) 하나의 변수에 여러 데이터를 저장할 수 있다.
'''
age = 10
print(age)
age = 20
print(age)
print()

name ="홍길동"
print(name, type(name)) # <class 'str'>
name= 10
print(name, type(name)) # <class 'int'>
name= True
print(name, type(name)) # <class 'bool'>
name= ["aa","bb"]
print(name, type(name)) #<class 'list'>
name= {"aa","bb"}
print(name, type(name)) #<class 'set'>
name= ("aa","bb")
print(name, type(name)) #<class 'tuple'>
name= {"name":"홍길동"}
print(name, type(name)) #<class 'dict'>
name = None
print(name, type(name))