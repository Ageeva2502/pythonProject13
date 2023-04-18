sum_all = 0
while True:
    try:
        kol_ticket = input('Сколько билетов вы хотите приобрести на конференцию? ')
        kol_ticket = int(kol_ticket)
        if type(kol_ticket) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(kol_ticket):
    i += 1
    while True:
        try:
            age_for_ticket = input(f'Введите возраст посетителя №{i}? ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('Билет бесплатный')
            elif 25 > age_for_ticket >= 18:
                sum_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                sum_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if kol_ticket > 3:
    price_all = sum_all - ((sum_all / 100) * 10)
    print(f'Сумма к оплате {sum_all} руб. с учетом 10%-ой скидки')
else:
    print(f'Сумма к оплате {sum_all} руб.')