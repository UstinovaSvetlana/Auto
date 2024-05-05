from address import Address
from Mailing  import Mailing # Импорт классов Address и Mailing из файла my_module

# Создание объектов адресов
to_address = Address("427620", "Глазов", "Пушкина", "10", "5")
from_address = Address("127000", "Москва", "Лермонтова", "20", "10")

# Создание почтового отправления
mailing = Mailing(to_address, from_address, 200, "ABCD987654321")

# Печать информации об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей")