while True:
    LESS_DEPOSIT = 0.10
    MORE_DEPOSIT = 0.25
    # количество бутылок каждого вида
    less = int(input("Сколько у вас бутылок объемом 1 литр и меньше? "))
    more = int(input("Сколько у вас бутылок объемом больше 1 литра? "))
    # сумма
    refund = less * LESS_DEPOSIT + more * MORE_DEPOSIT
    # результат
    print("Ваша выручка составит $%.2f." % refund)