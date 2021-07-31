import time
'''
def exchange_p(x): #알파벳으로 입력된 row 변환
    if x=='a':
        x='1'
    if x=='b':
        x='2'
    if x=='c':
        x='3'
    if x=='d':
        x='4'
    if x=='e':
        x='5'
    if x=='f':
        x='6'
    if x=='g':
        x='7'
    if x=='h':
        x='8'
    return x
'''
def check(x,y): # 이동한 곳 주어진 영역 안인지 확인
    if x>=1 and x<=8:
        if y>=1 and y<=8:
            return 'ok'
        else:
            return 'not ok'
    else:
        return 'not ok'

start_time= time.time()
place = input() # 처음 위치해 있는 장소 입력받기
x=int(ord(place[0]))-int(ord('a'))+1 # x,y 정수로 변환
y=int(place[1])

ways = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)] # 이동할 수 있는 모든 경우의 수
result=0
for way in ways:
    next_x=x+way[0]
    next_y=y+way[1]
    sign = check(next_x,next_y)
    if sign == 'ok':
        result+=1
print(result)

end_time = time.time()
print("time:", end_time-start_time)