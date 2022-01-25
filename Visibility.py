#가시성
class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items=[] #private 변수

    @property #property decorator 순겨진 변수를 반환하게 해줌
    def items(self):
        return self.__items

    def add_new_item(self,product):
        if type(product)==Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)

my_inventory=Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
print(my_inventory.get_number_of_items())

items=my_inventory.items #property decorator로 함수를 변수처험 호출
items.append(Product())
print(my_inventory.get_number_of_items())
