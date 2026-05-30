# 파일이름 :
# 작 성 자 :
players = []

def calc_grade(average):
    if average >= 0.300:
        return "S" 
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

    try:
        at_bat = int(input("타수: "))
        hit = int(input("안타: "))
    except ValueError:
        print("숫자만 입력하세요.")
        return
    
    if at_bat == 0:
        average = 0
    else:
        average = hit / at_bat

    players.append([name, at_bat, hit, average])
    print("선수 등록 완료!")

def show_players():
    if len(players) == 0:
        print("\n등록된 선수가 없습니다.")
        return
    print("\n=====선수 기록=====")

    labels = ["선수 이름", "타수", "안타", "타율"]

    for player in players:
        for i in range(4):

            if i == 3:
                print(f"{labels[i]}: {player[i]:.3f}")

            else:
                print(f"{labels[i]}: {player[i]}")

        grade = calc_grade(player[3])

        print(f"\n선수 이름: {labels[0]}")
        print(f"타수: {labels[1]}")
        print(f"안타: {labels[2]}")
        print(f"타율: {labels[3]}")
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

def save_file():

    try:
        with open("players.txt", "w",encoding="utf-8") as file:
            for player in players:
                file.write(
                    f"{player[0]}, {player[2]}, {player[3]:.3f}\n"
                )
        print("파일 저장 완료!")
    except FileNotFoundError:
        print("파일 오류가 발생했습니다.")

while True:

    print("\n===== ⚾ 야구 선수 기록 관리 시스템 =====")
    print("1. 선수 등록")
    print("2. 선수 전체 조회")
    print("3. 최고 타율 선수 분석")
    print("4. 팀 평균 타율 보기")
    print("5. 파일 저장")
    print("6. 프로그램 종료")

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
        save_file()

    elif menu == "6":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴 번호를 입력하세요.")
