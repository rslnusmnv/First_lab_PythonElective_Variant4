from random import randint


# Функция генерации телефонов
def generateRandomTelephone(number: int):
    telephones = []
    for i in range(number):
        result = randint(0, 9)
        if result == 7:
            result = "+7"
            lenTelephone = 10
        elif result == 8:
            result = "8"
            lenTelephone = 10
        elif result == 9:
            lenTelephone = 9
        else:
            lenTelephone = randint(1, 25)
        result = str(result)
        for j in range(lenTelephone):
            digit = str(randint(0, 9))
            result += digit
        telephones.append(result)
    return telephones


# Генерация и сохранения телефонов в текстовый файл с названием "telephones.txt"
number = 0
while number < 50:
    number = int(input("Введите количество генерируемых телефонов: "))
telephonesList = generateRandomTelephone(number)
print("Телефоны сгенерированы")
telephonesFile = open('telephones.txt', 'w')
for item in telephonesList:
    telephonesFile.write("%s\n" % item)
telephonesFile.close()
print("Сгенерированные телефонов записаны в текстовый файл 'telephones.txt'")

# Открытие файла с телефонами
telephonesFile = open('telephones.txt', 'r')
telephonesForAnalyze = telephonesFile.read()
telephonesForAnalyze = telephonesForAnalyze.splitlines()
print("Текстовый файл 'telephone.txt' открыт")

# Проверка на валидность телефонных номеров
correctTelephones = []
for element in telephonesForAnalyze:
    if (len(element) == 10 and element[0] == '9') or (
            len(element) == 11 and element[0] == '8') or (
            len(element) == 12 and element[0] == '+' and element[1] == '7'):
        correctTelephones.append(element)
print("Валидация проведена")

# Сохранение валидных телефонов в текстовый файл "correct.txt"
correctTelephonesFile = open('correct.txt', 'w')
for item in correctTelephones:
    correctTelephonesFile.write("%s\n" % item)
correctTelephonesFile.close()
print("Валидные телефоны записаны в текстовый файл 'correct.txt'")

# Подсчет статистики и запись статистики в текстовый файл "statistics.txt"
lenAllTelephones = len(telephonesList)
lenCorrectTelephones = len(correctTelephones)
different = lenAllTelephones - lenCorrectTelephones
statisticsFile = open('statistics.txt', 'w')
statisticsFile.write("Количество всех телефонов: %s\n" % lenAllTelephones)
statisticsFile.write("Количество валидных телефонов: %s\n" % lenCorrectTelephones)
statisticsFile.write("Количество невалидных телефонов: %s" % different)
statisticsFile.close()
print("Статистика записана в текстовый файл 'statistics.txt'")
