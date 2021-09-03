#볼링공 고르기
#두 사람이 서로 무게가 다른 볼링공을 고르려고 함
#무게가 같은 공 여러개 일 수 있지만 다른 공으로 간주
n,m = map(int,input().split()) #n,m값 입력받기
k = list(map(int,input().split())) #볼링공 무게 입력받기

result=0
for a in k: #A가 선택할 수 있는 공
    for b in k: #B가 선택할 수 있는 공
        if a != b: # 무게가 다를 경우
            result += 1

print(result//2) #출력값이 번호들의 '조합'의 수이기 떄문에 두번씩 세어진 경우 제거