#some_list = ['hello',23, 'jordan',7.90, 'true']
#for q in some_list:
   # print((type(q)))

##for t in my_list:
    #print(t+2)

   # my_list = [1, 'a', 'hello', 'pasha']
    #for spam in my_list:
       # print(len(spam))

        # spam = 'tehnikum'
        # for i in spam:
        # print(i)

        # name = 'pasha'
        # for item in name:
        # print(item)

        # nabor = ('1','2','a')
        # for b in nabor:
        # print(b)

        # p =['m','my',23]
        # for tor in p:
        #  print(tor)

#my_tuple = (6, 4,'2')
#for i in range(1,100):
   # print(my_tuple)

#users = ['masha', 'warning','amazing','android', 'the', 'clone', 'cake','moon']

#users_name_a = []
##if 'a' in s:
      #  users_name_a.append(s)
      #  print(s)


#print(users_name_a)

users = []
numbers = []
service = []
# непрерывноть с циклом while
while True:
    admin = input('что вы хотите сделать(номер, услуга или имя): ')


    # проверка введенного слова
    if admin == 'номер':
        new_number = input('введите номер: ')



        if new_number in numbers:
            print('такой номер уже есть')

        elif new_number not in numbers:
            # добавлен в список
            numbers.append(new_number)
    print('успешно')
    print(numbers)







spam = ['words','loki','water', 'mater']
spam2 = []

for i in spam:
    if 'm' in i:
        spam2.append(i)

print(spam2)