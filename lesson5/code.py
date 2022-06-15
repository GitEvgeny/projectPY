# Задание 1 --------------------------------------------------

my_f = open('test_1.txt', 'w', encoding="utf-8")
line = input('Введите текст: \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст: \n')
    if not line:
        break

my_f.close()
my_f = open('test_1.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()



# Задание 2 --------------------------------------------------

f = open('text_4.txt')
line = 0
for i in f:
    line += 1
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print(i,len(i),'симв.',word,'слов')
print('\nВсего строк:', line)
f.close()



# Задание 3 --------------------------------------------------

with open('text_3.txt', 'r', encoding="utf-8") as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')



# Задание 4 --------------------------------------------------

rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_44.txt", "w", encoding="utf-8") as new_file:
    with open("text_4.txt", encoding="utf-8") as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])



# Задание 5 --------------------------------------------------

def summary():
    try:
        with open('text_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()



# Задание 6 --------------------------------------------------

my_dict = {}
with open("text_6.txt", encoding="utf-8") as fobj:
    for line in fobj:
        name, stats = line.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i == " " or "9" >= i >= "0"]).split()))
        my_dict[name] = name_sum
print(f"{my_dict}")
