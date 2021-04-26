string= input( "Enter an input: " )
number= input( "Enter the number: " ) 

ans=list(string)
print(ans.pop(int(number))) #index의 값 제거 = pop 함수
print(ans)

