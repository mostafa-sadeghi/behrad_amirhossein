# a = 4
# b = 5

# if a > b :
#     print('a is greater than b')
# else:
#     print('a is lower than b')


# a = 4
# b = 5

# if a > b:
#     print('a is greater than b')
# elif a == b:
#     print('a is equal to b')
# else:
#     print('a is lower than b')


# a = 5
# b = 4

# if a >= b:
#     print("a is greater than or equal to b")

# if a > b or a == b:
#     print("a is greater than or equal to b")
# score = 22
# if score > 20 and score < 40:
#     print("go to level 2")

# if 22 < score < 40:
#     print("go to level 2")
'''
# یک برنامه بنویسید که سن داوطلب را دریافت نمایدو
اگر سن او کمتر از هشت سال بود
kid

اگر سن بین هشت تا 12 بود
junior

اگر سن بین 12 تا 18 بود
teenager

بالاتر از 18
adult
'''
# name = input('enter a name:> ')
# age = int(input('enter a age:> '))

# if age < 8:
#     print(f'{name}`s age is {age} and he/she is kid.')

# if age >= 8 and age < 12:
#     # if 8 <= age < 12:
#     print(f'{name}`s age is {age} and he/she is junior.')

# if age >= 12 and age < 18:
#     print(f'{name}`s age is {age} and he/she is teenager.')
# if age >= 18:
#     print(f'{name}`s age is {age} and he/she is adult.')

# برنامه ای بنویسید که 3 عدد را از ورودی دریافت نماید
# و در صورتی که عدد وارد شده زوج بوده و نیز بین ده تا صد باشد پیغام زیر را پرینت نماید
# even and ok
# در صورتی که عدد وارد شده فرد باشد و نیز بین پنجاه تا هشتاد باشد پیغام زیر را پرینت نماید
# odd and ok

# number1 = float(input('enter first number:> '))
# number2 = float(input('enter second number:> '))
# number3 = float(input('enter third number:> '))

# if number1 % 2 == 0 and (10 < number1 < 100):
#     print(f'{number1} is even and between 10 and 100')

# elif number1 % 2 != 0 and (50 < number1 < 80):
#     print(f'{number1} is odd and between 50 and 80')


# if number2 % 2 == 0 and (10 < number2 < 100):
#     print(f'{number2} is even and between 10 and 100')

# elif number2 % 2 != 0 and (50 < number2 < 80):
#     print(f'{number2} is odd and between 10 and 80')

# if number3 % 2 == 0 and (10 < number3 < 100):
#     print(f'{number3} is even and between 10 and 100')

# elif number3 % 2 != 0 and (50 < number3 < 80):
#     print(f'{number3} is odd and between 10 and 80')


# a = 1
# b = 3

# if a == b:
#     print('a and b are equal!!!')

# if a != b:
#     print('a and b are not equal!!!')


# name1 = 'behrad'
# name2 = 'amirhossein'

# if name1 == name2:
#     print('both names are the same')

# name1 = 'amirhossein'
# name2 = 'amirhossein'
# if name1 == name2:
#     print('both names are the same')

# name1 = input('enter your name:> ')
# name2 = input('enter your name:> ')

# if name1 == name2:
#     print('both names are the same')
# else:
#     print('both names are not the same')

# USER = 'admin'
# PASS = 'root'

# user_name = input('enter user name:> ')
# password = input('enter password:> ')

# if user_name == USER and password == PASS:
#     print("your user name and password is correct.")
#     print("your account is valid")
#     print('login was successful!!!')
# else:
#     print('you are`nt valid user')
#     print('sorry, you can`t login')


# bool datatype
# a = True
# if a:
#     print('a')

# b = False
# if b:
#     print('b')


# برنامه ای بنویسید که
# ده عدد از ورودی دریافت نماید
# و به لیستی اضافه کند
# اکنون دو لیست جدید بساز و در یکی ، اعداد فرد موجود در لیست اصلی را ذخیره کن
# و در لیست دوم، اعداد زوج موجود در لیست اصلی را ذخیره کن
# اعضای لیست اصلی را پرینت کن
# اعضای لیست دوم را پرینت کن
# اعضای لیست سوم را پرینت کن
# مجموع اعدا لیست اصلی را محاسبه و پرینت کن
# مجموع اعداد لیست دوم را پرینت کن
# مجموع اعداد لیست سوم را پرینت کن
# numbers = []
# n1 = float(input('enter a number: '))
# n2 = float(input('enter a number: '))
# n3 = float(input('enter a number: '))
# numbers.append(n1)
# numbers.append(n2)
# numbers.append(n3)
# print("all numbers in main list", numbers)
# even_numbers = []  # عدد های زوج
# odd_numbers = []  # عدد های فرد
# اگر باقی مانده تقسیم یک عدد بر دو مساوی صفر باشد، آنگاه عدد زوج است
# اگر باقی مانده تقسیم عددی بر دو صفر نلاید عدد فرد است
# if numbers[0] % 2 == 0:
#     even_numbers.append(numbers[0])
# else:
#     odd_numbers.append(numbers[0])
# if numbers[1] % 2 == 0:
#     even_numbers.append(numbers[1])
# else:
#     odd_numbers.append(numbers[1])
# if numbers[2] % 2 == 0:
#     even_numbers.append(numbers[2])
# else:
#     odd_numbers.append(numbers[2])
# print("even numbers : ", even_numbers)
# print("odd numbers : ", odd_numbers)

# تمرین اول

# مجموع اعداد لیست اصلی را محاسبه و پرینت کن
# مجموع اعداد لیست دوم را پرینت کن
# مجموع اعداد لیست سوم را پرینت کن




# تمرین دوم

# برنامه ای بنویسید که نام سه دوست را از ورودی بگیرد
# و در یک لیت ذخیره نماید
# سپس پیغامی مشابه زیر نمایش داده شود
# ali and reza and sina are friends.
friends = []
name1 = input('enter a name:> ')
name2 = input('enter a name:> ')
name3 = input('enter a name:> ')
friends.append(name1)
friends.append(name2)
friends.append(name3)

print(f'{name1} and {name2} and {name3} are firend.')



# نام شخص دیگری را از ورودی بگیرید و به لیست بالا اضافه نمائید
# نام شخصی را از ورودی بگیرد و از لیست با لا حذف نمائید.

name4 = input('enter a name: ')
friends.append(name4)

name = input('enter a name to delete:> ')
friends.remove(name)
print(friends)


# یادآوری
numbers = [1, 2, 3, 4, 5]

numbers.remove(4)
