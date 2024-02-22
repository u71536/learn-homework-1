"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str1, str2):


    if isinstance(str1, str) == True and isinstance(str2, str) == True:
        if str1 == str2:
            return 1
        elif str1 != str2 and str2 == "learn":
            return 3
        elif str1 != str2 and len(str1) > len(str2):
            return 2
    else:
        return 0

    
if __name__ == "__main__":
    print(main("Some text", "Some text"))
    print(main("Some more text", "Some text"))
    print(main("Some text", "learn"))
    print(main(4, "Some text"))
    print(main(4, 5.0))
