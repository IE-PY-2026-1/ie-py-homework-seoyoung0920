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
    player.append([name, at_bat, hit, average])

# 결과 출력
print("\n=== 선수 기록 ===")