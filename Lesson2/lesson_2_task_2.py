def is_year_leap(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Введите год для проверки: "))
if is_year_leap(year):
    print(year, "год - високосный")
else:
    print(year, "год - не високосный")