# 메뉴 확장 시 불편한 점 개선

menus = [["아이스 아메리카노", 0], ["카페 라떼", 0], ["유자차", 0]]  # [[메뉴, 수량], ...]
#prices = [2000, 2500, 2400]

#print(len(menus))
amount = int(input("몇 잔? "))

menu_lists = ""
for i in range(len(menus)):
    menu_lists = menu_lists + f"{i+1}) {menus[i][0]} "

for _ in range(amount):
    menu = input(f"{menu_lists}: ")
    if menu == "1":
        menus[0][1] = menus[0][1] + 1
    elif menu == "2":
        menus[1][1] = menus[1][1] + 1
    else:
        menus[2][1] = menus[2][1] + 1

print(f"총 금액은 {(menus[0][1] * 2000) + (menus[1][1] * 2500) + (menus[2][1] * 2400)}원 입니다.")

