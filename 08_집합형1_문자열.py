'''
  문자열
  1. 생성방법 4가지
  2. 특징: immutable(변경불가)
  3. 인덱싱과 슬라이싱
  4. 함수
'''
## 1. 문자열생성
m1 = "hello"
m2 = 'hello'
m3 = '''hello'''
m4 = """hello"""
print(m1, type(m1))
print(m2, type(m2))
print(m3, type(m3))
print(m4, type(m4))

# triple 용도
x ="asdfffffffffffffffffff" \
   "fffffffffffffffffffffffffff" \
   "fffffffffffffffffffffffffffffff" \
   "ffffffffffffffffffffffffffffffffff" \
   "ffffffffffffffffff"
print(x)
x2 ='''eeeeeeeeeeeeeeeeeee
eeeeeeeeeeeeeeeeeeeeeeeeeee
eeeeeeeeeeeeeeeeeeeeeeeeeeeee
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
eeeeeeeeee'''
print(x2)

xx = "<html><body><p>hello</p>"
xx2 = '''
    <html>
      <body>
        <p>hell</p>
      </body>
    </html>    
'''
print(xx2)