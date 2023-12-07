import datetime
class Product:
    def __init__(self, idx, name, cost=0, category="none", date=datetime.date.today()):
        self.id = idx
        self.name = name
        self.cost = cost
        self.category = category
        self.date = date