import kiosk  # 파일 분리 (키오스크 모듈)

menu_lists = "".join([f"{i + 1}) {kiosk.menus[i][0]} " for i in range(len(kiosk.menus))])
menu_lists = menu_lists + f"{len(kiosk.menus) + 1}) 주문 종료 : "

while True:
    menu = input(menu_lists)
    if 0 < int(menu) <= len(kiosk.menus):  # 1 ~ 4
        kiosk.select_menu(int(menu) - 1)
    elif menu == "5":
        print("주문을 종료합니다")
        break
    else:
        print("잘못된 주문입니다")

kiosk.print_receipt()
print(f"번호표 : {kiosk.get_ticket_number()}")