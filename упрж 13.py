
CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME =10
CENTS_PER_NICKEL =5


cents = int(input("Введите сумму в центах: "))


print(" ", cents // CENTS_PER_TOONIE, "двухдолларовых монет")
cents = cents % CENTS_PER_TOONIE


print(" ", cents // CENTS_PER_LOONIE, "однодолларовых монет")
cents = cents % CENTS_PER_LOONIE
print(" ", cents // CENTS_PER_QUARTER, "25–центовых монет")
cents = cents % CENTS_PER_QUARTER
print(" ", cents // CENTS_PER_DIME, "10–центовых монет")
cents = cents % CENTS_PER_DIME
print(" ", cents // CENTS_PER_NICKEL, "5–центовых монет")
cents = cents % CENTS_PER_NICKEL
# Отобразим остаток в центах
print(" ", cents, "центов")