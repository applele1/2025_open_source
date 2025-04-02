# 리스트 -> 메뉴 리스트

menus = [["아이스 아메리카노", 0], ["카페 라떼", 0], ["유자차", 0]]  # [[메뉴, 수량], ...]
#prices = [2000, 2500, 2400]

amount = int(input("몇 잔? "))

for _ in range(amount):
    menu = input(f"1) {menus[0][0]}   2) {menus[1][0]}   3) {menus[2][0]} : ")
    if menu == "1":
        menus[0][1] = menus[0][1] + 1
    elif menu == "2":
        menus[1][1] = menus[1][1] + 1
    else:
        menus[2][1] = menus[2][1] + 1

print(f"총 금액은 {(menus[0][1] * 2000) + (menus[1][1] * 2500) + (menus[2][1] * 2400)}원 입니다.")

