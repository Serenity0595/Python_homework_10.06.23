a = int(input())

c = a % 1000 #Вторая часть числа
b = int((a - c) / 1000) #Первая часть числа
d1 = b % 10
b = b // 10
d2 = b % 10
b = b // 10
d3 = c % 10
c = c // 10
d4 = c % 10
c = c // 10

second_numb = c + d3 + d4
first_numb = b + d1 + d2

if first_numb % second_numb == 0:
    print('YES')
else:
    print('NO')