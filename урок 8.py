# CLASS
class car:
    #  ХАРАКТЕРИСТИКА ДЛЯ КЛАССОВ
    def __init__(self, model, color,engine,koleso, tonirovka= 'нету'):
        """Назначаются характеристики"""
        self.model = model
        self.color = color
        self.engine = engine
        self.koleso = koleso
        self.tonirovka = tonirovka

    # МЕТОД ЕЗДЫ
    def drive(self):
        return 'поехали'


    # МЕТОД ОСТАНОВКИ
    def stop(self):
        return 'stoop'


    #МЕТОД НАТЯЖКИ ТОНИРОВКИ
    def toner(self, percet):
        self.tonirovka = percet

        return f'{self.model} натянул тонировку {percet} %'


# Создание обьекта к классу car
tesla = car(model='tesla', color='white',engine='electro', koleso=4)
captiva = car(model='captiva', color='black',engine='turbo', koleso=4)

print(tesla.tonirovka)
print(tesla.toner(80))

# Вызов методов классов : переменная.метод()
svetofor = 'red'


if svetofor == 'red':
    # ВЫВОД ХАРАКТЕРИСТИК - ПЕРЕМЕННАЯ.ХАРАКТЕРИСТИКА
    print(tesla.drive(), tesla.model, tesla.color)
    print(captiva.stop(), tesla.model, captiva.color)


# на теслу натянули тонировку

print(tesla.toner(80))
