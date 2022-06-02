# задание 1

a = 2
b = 3
c = a + b
print(c)
stroka = input("Введите строку: ")
chislo = int(input("Введите число: "))
print(stroka)
print(chislo)


# задание 2


t = int(input("Введите время в секундах "))
h = t // 3600
m = (t - h * 3600) // 60
s = t - (h * 3600 + m * 60)
print(f"Время в формате чч:мм:сс   {h} : {m} : {s}")


# задание 3


n = int(input("Введите число - "))
q = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % q)


# задание 4


n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break


# задание 7


a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
