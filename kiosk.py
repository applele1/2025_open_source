# 주문 할 때마다 주문 상황을 디스플레이

menus = [["아이스 아메리카노", 0], ["카페 라떼", 0], ["유자차", 0], ["자바칩 프라푸치노", 0]]  # [[메뉴, 수량], ...]
prices = [2000, 2500, 2400, 7000]

amount = int(input("몇 잔? "))

menu_lists = ""
for i in range(len(menus)):
    menu_lists = menu_lists + f"{i+1}) {menus[i][0]} "

for _ in range(amount):
    menu = input(f"{menu_lists}: ")
    if menu == "1":
        menus[0][1] = menus[0][1] + 1
        print(f"{menus[0][0]} {menus[0][1]}개 주문...")
    elif menu == "2":
        menus[1][1] = menus[1][1] + 1
        print(f"{menus[1][0]} {menus[1][1]}개 주문...")
    elif menu == "3":
        menus[2][1] = menus[2][1] + 1
        print(f"{menus[2][0]} {menus[2][1]}개 주문...")
    elif menu == "4":
        menus[3][1] = menus[3][1] + 1
        print(f"{menus[3][0]} {menus[3][1]}개 주문...")
    else:
        print("잘못된 주문입니다")


total_price = 0
for j in range(len(menus)):
    if menus[j][1] > 0:  # 각 메뉴들의 수량이 1 이상이면
        total_price = total_price + (menus[j][1]* prices[j])  # 가격 리스트에서 가격 추출해서 합산

print(f"총 금액은 {total_price}원 입니다.")
#print(f"총 금액은 {(menus[0][1] * 2000) + (menus[1][1] * 2500) + (menus[2][1] * 2400)}원 입니다.")
