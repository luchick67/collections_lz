import pandas as pd
import numpy as np

df = pd.DataFrame(columns=["ФИО", "Адрес", "Телефон", "Дата рождения"])

while True:
    print("\n1-Показать, 2-Добавить, 3-Удалить, 4-Изменить, 5-Выход")
    b = input("Действие: ")

    if b == "1":
        print(df)

    elif b == "2":
       
        df.loc[len(df)] = [
            input("ФИО: "),
            input("Адрес: "),
            input("Телефон: "),
            input("Дата рождения: "),
        ]

    elif b == "3":
        c = int(input("Индекс для удаления: "))
        df = df.drop(c).reset_index(drop=True)  

    elif b == "4":
        c = int(input("Индекс строки: "))
        d = input("Какое поле менять (ФИО/Адрес/Телефон/Дата рождения): ")
        df.at[c, d] = input("Новое значение: ") 
    elif b == "5":
        break
