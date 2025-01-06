class Prodcut:
    def __init__(self, name, price,stock):
        self.name = name
        self.__price = price
        self.__stock = stock
    def addstock(self,add):
                self.__stock += add
    def checkstock(self):
        return f"ชื่อสินค้า {self.name} ราคา {self.__price} มีจำนวน {self.__stock} ชิ้น"
    def editprice(self,price):
            self.__price = price
  
pd1 = Prodcut("สินค้า1", 500, 10)
pd1.addstock(-5)
pd1.editprice (100)
print(pd1.checkstock())
    
