'''class for items'''
from sprites import ItemSprites

class Item():
    def __init__(self, name: str = 'item', quantity: int = 0) -> None:
        self.name = name
        self.quantity = quantity
    def use(self, *args, **kwargs):
        ...
    def __str__(self):
        return f'Name: {self.name}, Quantity: {self.quantity}'

class WeponItem(Item):
    def __init__(self, name: str = 'item', quantity: int = 0) -> None:
        super().__init__(name, quantity)

class ItemData():
    def __init__(self, name: str, quantity: int = 1, item_type: Item = Item):
        self.name = name
        self.quantity = quantity
        self.item_type = item_type

items: dict[str, ItemData] = {
    'sword':ItemData('sword'),
    'battleAxe':ItemData('battleAxe'),
    'mace':ItemData('mace'),
    'bronzeHelm':ItemData('bronzeHelm'),
    'woodenShield':ItemData('woodenShield'),
    'goldBar':ItemData('goldBar'),
}