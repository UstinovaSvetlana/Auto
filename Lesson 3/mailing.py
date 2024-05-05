class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address  # Поле типа Address для адреса получателя
        self.from_address = from_address  # Поле типа Address для адреса отправителя
        self.cost = cost  # Стоимость почтового отправления (число)
        self.track = track  # Номер отслеживания (строка)