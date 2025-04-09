# 영수증 개선 (문자열 포맷팅. f-string)

def select_menu(i):
    menus[i][1] = menus[i][1] + 1
    print(f"{menus[i][0]} {menus[i][1]}잔 주문...")
    subtotal = 0
    for j in range(len(menus)):
        subtotal = subtotal + (prices[j] * menus[j][1])
    print(f"소계 : {subtotal}")


menus = [["아이스 아메리카노", 0], ["카페 라떼", 0], ["유자차", 0], ["자바칩 프라푸치노", 0]]  # [[메뉴, 수량], ...]
prices = [2000, 2500, 2400, 7000]

menu_lists = ""
for i in range(len(menus)):
    menu_lists = menu_lists + f"{i+1}) {menus[i][0]} "

while True:
    menu = input(f"{menu_lists}{len(menus)+1}) 주문 종료 : ")
    if menu == "1":
        select_menu(0)
    elif menu == "2":
        select_menu(1)
    elif menu == "3":
        select_menu(2)
    elif menu == "4":
        select_menu(3)
    elif menu == "5":
        print("주문을 종료합니다")
        break
    else:
        print("잘못된 주문입니다")


print("=" * 38)
#print("품명\n단가 / 수량 / 금액")
total_price = 0
for j in range(len(menus)):
    if menus[j][1] > 0:  # 각 메뉴들의 수량이 1 이상이면
        print(f"품명: {menus[j][0]}\n\t단가: {prices[j]} / 수량: {menus[j][1]:2} / 금액: {menus[j][1]* prices[j]:6}")
        total_price = total_price + (menus[j][1]* prices[j])  # 가격 리스트에서 가격 추출해서 합산

print(f"총 금액은 {total_price}원 입니다.")
