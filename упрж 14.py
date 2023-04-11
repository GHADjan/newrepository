IN_PER_FT = 12
CM_PER_IN = 2.54
# Запрашиваем рост у пользователя
print("Введите рост:")
feet = int(input("Количество футов: "))
inches = int(input("Количество дюймов: "))
# Переводим в сантиметры
cm = (feet * IN_PER_FT + inches) * CM_PER_IN
# Отобразим результат
print("Ваш рост в сантиметрах:", cm)