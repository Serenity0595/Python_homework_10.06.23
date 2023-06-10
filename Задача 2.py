a = int(input())

d1 = a % 10
a = a // 10
d2 = a % 10
a = a // 10

print("Сумма цифр числа:", a + d1 + d2)