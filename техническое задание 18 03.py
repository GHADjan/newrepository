class student:
    def __init__(self, name, firstname, group, spisok_ocenok=[]):
        self.name = name
        self.firstname = firstname
        self.group = group
        self.spisok_ocenok = spisok_ocenok

    # ДОБАВЛЕНИЕ ОЦЕНКИ
    def dobavlenie(self, ocenka):
        self.spisok_ocenok.append(ocenka)

        return f'{self.name, self.firstname} получил оценку {ocenka}:'

    # удаление оценки
    def udalenkie(self, ocenka):
        self.spisok_ocenok.remove(ocenka)
        return f'У студента {self.name, self.firstname} удалили оценку {ocenka}:'

    # средняя оценка
    def sredniy_ball(self):
        result = sum(self.spisok_ocenok) / len(self.spisok_ocenok)
        return f'Средний балл у {self.name, self.firstname, result}'
    def ocenki(self):
        return self.spisok_ocenok


# студент

student1 = student(name="pasha", firstname="pavlov", group="h123")


# ПАША ПОЛУЧИЛ ОЦЕНКУ

print(student1.dobavlenie(5), student1.ocenki())
print(student1.dobavlenie(5), student1.ocenki())
print(student1.dobavlenie(2), student1.ocenki())
print(student1.dobavlenie(3), student1.ocenki())
print(student1.udalenkie(5), student1.ocenki())
# СРЕДНИЙ БАЛЛ У ПАШИ
print(student1.sredniy_ball())