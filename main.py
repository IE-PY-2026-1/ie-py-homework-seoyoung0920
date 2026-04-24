# 파일이름 :
# 작 성 자 :
players = []

team_name = input("팀 이름을 입력하세요: ")
bonus_rate = 0.1

count = int(input("등록할 선수 수를 입력하세요 (최소 3명): "))

for i in range(count):
    print(f"\n{i+1}번째 선수 입력")
    
    name = input("선수 이름: ")
    at_bat = int(input("타수: "))
    hit = int(input("안타: "))

    if at_bat == 0:
        average = 0.0
    else:
        average = hit / at_bat

    players.append([name, at_bat, hit, average])

players.sort(key=lambda x: x[3], reverse=True)

total_avg = 0

print(f"\n {team_name} 선수 기록")

for player in players:
    name, at_bat, hit, average = player

    total_avg += average

    if average >= 0.300:
        grade = "S"
    elif average >= 0.250:
        grade = "A"
    elif average >= 0.200:
        grade = "B"
    elif average >= 0.150:
        grade = "C"
    else:
        grade ="F"

    if average >= 0.300 and hit >= 20:
        bonus = average * bonus_rate
        title = f"우수 타자 (+보너스 타율 {bonus:.3f})"
    elif average < 0.150 or at_bat < 5:
        title = "훈련 필요"
    else:
        title = "일반 선수"

    print(f"\n이름: {name}")
    print(f"타수: {at_bat}, 안타: {hit}")
    print(f"타율: {average:.3f}")
    print(f"등급: {grade}")
    print(f"칭호: {title}")

team_avg = total_avg / len(players)
print(f"\n 팀 평균 타율: {team_avg:.3f}")
