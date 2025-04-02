# 메뉴 : 1) 아이스 아메리카노  2) 카페 라떼
# 가격 : 1) 2000원   2) 2500원

menu01 = 0
menu02 = 0
amount = int(input("몇 잔? "))

for _ in range(amount):  # 입력 횟수 만큼 반복
    menu = input("1) 아이스 아메리카노  2) 카페 라떼 : ")
    if menu == "1":
        menu01 = menu01 + 1
    else:
        menu02 = menu02 + 1

print(f"총 금액은 {(menu01 * 2000) + (menu02 * 2500)}원 입니다.")