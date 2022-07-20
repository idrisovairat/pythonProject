class worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surename}"

    def get_full_name(self):
        return f"{sum(self._income.values())}"

manafer = Position('Tom', 'Curse', 'CEO', 500000, 125000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())
