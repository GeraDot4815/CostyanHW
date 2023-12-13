import datetime
class Product:
    def __init__(self, id, name, cost, category=None, date=None):
        self.id = id
        self.name = name
        self.cost = cost
        self.category = category if category!=None else "none"
        self.date = date if date!=None else datetime.date.today().strftime("%d.%m.%Y")