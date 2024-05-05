def bank(X, Y):
    # Изначальная сумма на счету пользователя
    total = X

    for _ in range(Y):
        # Вычисляем сумму процентов за текущий год
        percent = total * 0.10
        # Добавляем проценты к сумме на счету
        total += percent

    return total

# Пример использования функции
X = float(input("Введите размер вклада: "))
Y = int(input("Введите срок вклада в годах: "))
result = bank(X, Y)
print("Сумма на счету после", Y, "лет:", result)