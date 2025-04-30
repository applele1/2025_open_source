# 번호표 (ticket.txt)

def select_menu(i):
    menus[i][1] = menus[i][1] + 1
    print(f"{menus[i][0]} {menus[i][1]}잔 주문...")
    subtotal = 0
    for j in range(len(menus)):
        subtotal = subtotal + (menus[j][2] * menus[j][1])  # (단가 * 수량) 누적
    print(f"소계 : {subtotal}")


def print_receipt():
    print("=" * 38)
    total_price = 0
    lines = list()  # 영수증에 출력될 내용(문자열) 저장
    with open("receipt.txt", "w") as fp:
        for j in range(len(menus)):
            if menus[j][1] > 0:  # 각 메뉴들의 수량이 1 이상이면
                line = f"품명: {menus[j][0]}\n\t단가: {menus[j][2]} / 수량: {menus[j][1]:2} / 금액: {menus[j][1] * menus[j][2]:6}\n"
                lines.append(line)
                total_price = total_price + (menus[j][1] * menus[j][2])  # 가격 리스트에서 가격 추출해서 합산
        lines.append(f"총 금액은 {total_price}원 입니다.\n")


        receipt = input(f"1) 영수증 출력  2) 영수증 미출력 : ")
        if receipt == "1":
            print(''.join(lines))
            #fp.write(lines)  # error not list must be str
            fp.write(''.join(lines))
        else:
            print(''.join(lines))
            # ['품명: 아이스 아메리카노\n\t단가: 2000 / 수량:  1 / 금액:   2000\n', '품명: 자바칩 프라푸치노\n\t단가: 7000 / 수량:  2 / 금액:  14000\n', '총 금액은 16000원 입니다.\n']


menus = [["아이스 아메리카노", 0, 2000], ["카페 라떼", 0, 2500], ["유자차", 0, 2400], ["자바칩 프라푸치노", 0, 7000]]  # [[메뉴, 수량, 단가], ...]
# menus = [
#     ["아이스 아메리카노", 0, 2000],
#     ["카페 라떼", 0, 2500]
# ]  # [[메뉴, 수량, 단가], ...]

menu_lists = ""
for i in range(len(menus)):
    menu_lists = menu_lists + f"{i+1}) {menus[i][0]} "
menu_lists = menu_lists + f"{len(menus)+1}) 주문 종료 : "

while True:
    #menu = input(f"{menu_lists}{len(menus)+1}) 주문 종료 : ")
    menu = input(menu_lists)
    if 0 < int(menu) <= len(menus):  # 1 ~ 4
        select_menu(int(menu)-1)
    #elif menu == "5":
    #elif menu == len(menus)+1:  # menu는 str, 우변의 값은 int, type이 서로 달라 항상 False
    elif menu == str(len(menus) + 1):  # 문자로 형변환
        print("주문을 종료합니다")
        break
    else:
        print("잘못된 주문입니다")


print_receipt()
with open("ticket.txt", "r") as fp1:
    number = int(fp1.readlines()[0])
    number = number + 1
    print(f"번호표 : {number}")
    with open("ticket.txt", "w") as fp2:
        fp2.write(str(number))
