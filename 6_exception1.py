"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    user_input = input("Как дела?").lower()

    while user_input != "хорошо":
        try:
            user_input = input("Давайте еще раз. Как дела? ").lower()
        except:
            print("\nПока!")
            break


if __name__ == "__main__":
    hello_user()
