"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def hello_user():
    user_input = input("Как дела?").lower()

    while user_input != "хорошо":
       user_input = input("Давайте еще раз. Как у вас дела?")

    
if __name__ == "__main__":
    hello_user()
