# 영수증 코드 업데이트 (딕셔너리)

def select_menu(m):
    amounts[m] = amounts[m] + 1
    print(f"{m} {amounts[m]}잔 주문...")
    subtotal = 0
    for menu, price in prices.items():
        subtotal = subtotal + (price * amounts[menu])
    print(f"소계 : {subtotal}")


def print_receipt():
    print("=" * 38)
    total_price = 0
    #for j in range(len(menus)):
    for menu, amount in amounts.items():
        #if menus[j][1] > 0:  # 각 메뉴들의 수량이 1 이상이면
        if amount > 0:  # 각 메뉴들의 수량이 1 이상이면
            #print(f"품명: {menus[j][0]}\n\t단가: {prices[j]} / 수량: {menus[j][1]:2} / 금액: {menus[j][1] * prices[j]:6}")
            print(f"품명: {menu}\n\t단가: {prices[menu]} / 수량: {amount:2} / 금액: {amount * prices[menu]:6}")
            #total_price = total_price + (menus[j][1] * prices[j])  # 가격 리스트에서 가격 추출해서 합산
            total_price = total_price + (amount * prices[menu])
    print(f"총 금액은 {total_price}원 입니다.")


prices = {
    'Ice Americano': 2000,
    'Caffe Latte': 2500,
    'Citron Tea': 2400,
    'Java Chip Frappuccino': 7000
}
amounts = {
    'Ice Americano': 0,
    'Caffe Latte': 0,
    'Citron Tea': 0,
    'Java Chip Frappuccino': 0
}

menu_lists = ""
for i, m in enumerate(amounts.keys()):  # 인덱스 및 메뉴 이름 추출
    menu_lists = menu_lists + f"{i+1}) {m} "

while True:
    menu = input(f"{menu_lists}{len(amounts)+1}) 주문 종료 : ")
    #if 0 < int(menu) <= len(amounts):  # 1 ~ 4
    if menu == "1":
        select_menu('Ice Americano')
    elif menu == "2":
        select_menu('Caffe Latte')
    elif menu == "3":
        select_menu('Citron Tea')
    elif menu == "4":
        select_menu('Java Chip Frappuccino')
    elif menu == "5":
        print("주문을 종료합니다")
        break
    else:
        print("잘못된 주문입니다")


print_receipt()