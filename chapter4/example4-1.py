import time
def search_w(w, UD, LR): # 입력받은 LRUD를 통해 각 축방향으로 이동하는 함수
    if w == 'U':
        UD-=1
    if w == 'D':
        UD+=1
    if w == 'L':
        LR -= 1
    if w == 'R':
        LR += 1
    return UD,LR

def check_w(n,UD,LR): # 정해진 정사각형 공간을 벗어나는 움직임인지 확인
    if UD<1:
        UD+=1
    if UD>n:
        UD-=1
    if LR<1:
        LR+=1
    if LR>n:
        LR-=1
    return UD, LR

start_time= time.time()
n = int(input()) # 정사각형의 크기 N입력받기
way = input().split() # LRUD를 띄어쓰기를 기준으로 입력받기
UD =1 #처음 위치한 x=1,y=1
LR =1
for w in way: #입력받은 way만큼 반복
    UD,LR = search_w(w,UD,LR)
    UD,LR = check_w(n,UD,LR)

print(UD,LR)

end_time = time.time()
print("time:", end_time-start_time)
