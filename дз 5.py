# ВОЗВОДИМ В СТЕПЕНЬ
numbers = [1, 2, 3, 4, 5]
numbers1 = [i ** 2 for i in numbers]
print(numbers1)


# CAPS LOCK
words = ['car', 'mike', 'jordan']
words1 = [o.upper() for o in words]
print(words1)



# ЧЕРЕЗ МАЛЕНЬКИЕ БУКВЫ
slova = ['CAR','MIKE','JORDAN']
slova1 = [u.lower() for u in slova]
print(slova1)



# четные числа
nums = [i for i in range(1,11) if i % 2 == 0]
print(nums)



# СЛОВА С БУКВОЙ "O"
names = ['jordan', 'pasha', 'nike']
names2 = [i for i in names if 'o' in i]
print(names2)



# УМНОЖИТЬ НА 2
chislo = [1,2,3,4,5]
chislo1 = [q*2 for q in chislo]
print(chislo1)



# вторая буквы слов
imena = ['jordan', 'pasha', 'nike']
imena1 = [w[1] for w in imena]
print(imena1)