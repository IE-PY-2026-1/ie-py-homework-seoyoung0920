# 파일이름 :
# 작 성 자 :
players = []

# 등록할 선수 수 입력
count = int(input("등록할 선수 수를 입력하세요: "))

# 선수 정보 입력
for i in range(count):
    print(f"\n{i+1}번째 선수 입력")
    
    name = input("선수 이름: ")
    at_bat = int(input("타수: "))
    hit = int(input("안타: "))
    
    # 타율 계산
    if at_bat == 0:
        average = 0
    else:
        average = hit / at_bat
    
    #선수 데이터 리스트에 저장
    player = [name, at_bat, hit, average]
    players.append([name, at_bat, hit, average])

# 결과 출력
print("\n=== 선수 기록 ===")

for player in range(len(players)):
    player = players[i]
    name = player[0]
    at_bat = player[1]
    hit = player[2]
    average = player[3]
    
    # 등급 판정 (높은 기준부터)
    if average >= 0.300:
        grade = "S"
    elif average >= 0.250:
        grade = "A"
    elif average >= 0.200:
        grade = "B"
    elif average >= 0.150:
        grade = "C"
    else:
        grade = "F"
    
    # 결과 출력
    print(f"\n선수 이름: {name}")
    print(f"타수: {at_bat}")
    print(f"안타: {hit}")
    print(f"타율: {average:.3f}")
    print(f"등급: {grade}")
    
    # 우수 선수 칭호
    if average >= 0.300:
        print("👉 우수 타자!")