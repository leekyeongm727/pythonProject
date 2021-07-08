'''각 행마다 가장 작은 값뽑고-> 그 중 가장 큰 값'''
n,m= map(int,input().split()) #map 관련 함수 책 참고

data=[] # 각 행에서 뽑아낸 min값 저장할 list
for x in range(n):  # 행의 개수 n만큼 반복
    m_number = list(map(int,input().split()))  #공백으로 구분된 리스트로 m개의 값 입력받기
    min_data = min(m_number) #매 행마다 가장 작은 수 뽑아내기
    data.append(min_data) # 만들어놓은 list에 작은 값 저장
    if len(m_number) > m:
        print("입력한 열의 개수가 주어진 M보다 크다")
        break
    if len(m_number) < m:
        print("입력한 열의 개수가 주어진 M보다 작다")
        break
result = max(data) #각 행마다 뽑아낸 작은 값들 중 max값 뽑아내기
print(result)


