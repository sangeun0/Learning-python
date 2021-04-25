A= list(input("enter the string: "))
B= list(input("enter the string: "))
n= int(input("enter the number: "))

del[B[0:n]] #원하는 인덱스 제거해주는 함수 del
            #0부터 n까지 인덱싱
string= A[0:n]+B
print(string)
