# 파일이름 :
# 작 성 자 :
players = []

def calc_grade(average):
    if average >= 0.300:
        return "A" 
    elif average >= 0.250:
        return "A"
    elif average >= 0.200:
        return "B"
    elif average >= 0.150:
        return "C"
    else:
        return "F"
    
def add_players():

    global players
    print("\n[선수 등록]")

    name = input("선수 이름: ")
    at_bat = int(input("타수: "))
    hit = int(input("안타: "))

    if at_bat == 0:
        average = 0
    else:
        average = hit / at_bat

    players.append([name, at_bat,hit, average])
    print("선수 등록 완료!")

def show_players():
    if len(players) == 0:
        print("\n등록된 선수가 없습니다.")
        return
    print("\n=====선수 기록=====")

    for player in players:
        name = player[0]
        at_bat = player[1]
        hit =player[2]
        average = player[3]

        grade = calc_grade(average)

        print(f"\n선수 이름: {name}")
        print(f"타수: {at_bat}")
        print(f"안타: {hit}")
        print(f"타율: {average:.3f}")
        print(f"등급: {grade}")

def best_player():
    if len(players) == 0:
        print("\n등록된 선수가 없습니다.")
        return
    
    best = max(players, key=lambda x:x[3])
    print("🏆최고 타율 선수")

    print(f"선수 이름: {best[0]}")
    print(f"타율: {best[3]:.3f}")

def team_average():
    if len(players) == 0:
        print("\n등록된 선수가 없습니다.")
        return
    
    total = 0

    for player in players:
        total += player[3]

    avg = total / len(players)

    print(f"📊팀 평균 타율: {avg:.3f}")

while True:

    print("\n===== ⚾ 야구 선수 기록 관리 시스템 =====")
    print("1. 선수 등록")
    print("2. 선수 전체 조회")
    print("3. 최고 타율 선수 분석")
    print("팀 평균 타율 보기")
    print("프로그램 종료")

    menu = input("메뉴 선택: ")

    if menu == "1":
        add_players()

    elif menu == "2":
        show_players()

    elif menu == "3":
        best_player()
    
    elif menu =="4":
        team_average()

    elif menu == "5":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다.")
