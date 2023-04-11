# nums =[12212, 123123 ,4356, 456756, 2354364, 'asasf']
# nums2 = [i*2 for i in nums]
# print(nums2)






# LIST COMPREHENSION
#name = 'pasha'
#n = []
#for item in name:
    #n.append(item
#print(n)
#name1 = 'pasha'
#n2 = [x for x in name1]
#print(n)







#nums = [i for i in range(1,11)]
#chotnie = [num for num in nums if num %2==0]
#nechotnie = [num for num in nums if num %2!=0]
#print(nechotnie, chotnie,)



#names = ['jordan', 'pasha', 'nike']
#names2= []
#for name in names:
 #   if 'o' in name:
 #       names2.append(name)
#print(names2)


#names = ['jordan', 'pasha', 'nike']
#names2 = [i for i in names if 'o' in i]
#print(names2)






#names = ['pavel', 'sasha','jordan', 'pasha']
#answer = [i[0] for i in names]
#print(answer)






#nums1 = [i for i in range(1,21)]
#nums2 = [i for i in nums1 if i % 2 == 0]
#print(nums2)


usernames = []
while True:
    k = input('введите имя: ')
    if k in usernames:
        print('этот пользователь уже есть, попробуйте другой')
    else:
        usernames.append(k)
        print(f'{k} успешно добавлен')
        print(usernames)






















