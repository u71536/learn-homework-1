"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


user_age = input()
kindergarden = 5
school = 18
uni = 23

def main(age):
    age = int(age)

    if age <= kindergarden:
        return (f"Ваш возраст {age}. Вы должны учиться в детском саду!")
    elif age <= school:
        return (f"Ваш возраст {age}. Вы должны учиться в школе!")
    elif age <= uni:
        return (f"Ваш возраст {age}. Вы должны учиться в университете!")
    else:
        return (f"Ваш возраст {age}. Вы должны работать!")

if __name__ == "__main__":
  print(main(user_age))
