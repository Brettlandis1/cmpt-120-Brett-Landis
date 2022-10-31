
class Product:
 # init method or constructor
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantiy = quantity

    # Sample Method
    def getInfo(self):
        print('Product info:')
        print("Name: ", self._name)
        print("Price: ", self._price)
        print("Quantity: ", self._quantiy)
