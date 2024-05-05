class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

# Пример использования класса Smartphone
phone = Smartphone("Samsung", "Galaxy S8", "+7900234567")
print("Марка телефона:", phone.brand)
print("Модель телефона:", phone.model)
print("Абонентский номер:", phone.phone_number)