"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

all_phones_sales_sum = 0
all_phones_sales_avg = 0


def main(sales):
    sales_sum = 0
    for sale in sales:
        sales_sum += sale
    return sales_sum


for item in phones:
    sales_sum = main(item['items_sold'])
    sales_avg = sales_sum / len(item['items_sold'])
    print(f"Сумма покупок {item['product']}: {round(sales_sum, 2)}")
    print(f"Среднее кол-во покупок {item['product']}: {round(sales_avg, 2)}")
    all_phones_sales_sum += sales_sum
    all_phones_sales_avg += len(item['items_sold'])

print(f'Сумма покупок всех телефонов: {all_phones_sales_sum}')
print(f'Среднее количество покупок всех телефонов: {all_phones_sales_sum / all_phones_sales_avg}')




# if __name__ == "__main__":
#     main(phones['items_sold'])
