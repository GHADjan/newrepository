while True:
    nalog = 0.05
    chay = 0.18

    cost = float(input('введите сумму счета: '))

    nalog1 = cost * nalog
    chay1 = cost * chay
    total = cost + nalog1 + chay1

    # результат

    print("налог составил: %.2f" % (nalog1), " чаевые - %.2f" % (chay1), "общая сумма заказа: %.2f" % (total))
