from smartphone import Smartphone


# Создание списка экземпляров класса Smartphone
catalog = [
    Smartphone("Samsung", "Galaxy S8", "+79043159543"),
    Smartphone("Apple", "iPhone 12", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"),
    Smartphone("OnePlus", "9 Pro", "+79456789012"),
    Smartphone("Google", "Pixel 5", "+79567890123")
]

# Печать всего каталога
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")