class Product:
    def init(self,brand,name,price,stock):
        self.brand = brand
        self.name = name
        self.price = price
        self.stock = stock

    def Edit(self,Amount):
        if Amount == "Stock":
            print(f"เพิ่มสต็อกสินค้า {self.name}")
            Amount_stock = int(input("ใส่จำนวนสต็อกที่ต้องการเพิ่ม: "))
            self.stock += Amount_stock
            print(f"เพิ่มสต็อกแล้ว")
        elif Amount == "Price":
            print(f"เปลี่ยนราคาสินค้า {self.name}")
            Amount_price = int(input("ใส่ราคา: "))
            self.price = Amount_price
        else:
            print("ใส่จำนวนบวก")

    def check(self):
        return f"แบรนด์ {self.brand}\nชื่อสินค้า {self.name}\nราคา {self.price} บาท\nสต็อก {self.stock} ชิ้น"

class Mobile(Product):
    def init(self,brand,name,price,stock,system):
        super().init(brand,name,price,stock)
        self.system = system
    def showmobile(self):
        return f"{super().check()}\nระบบปฏิบัติการ {self.system}"

class Notebook(Product):
    def init(self,brand,name,price,stock,cpu):
        super().init(brand,name,price,stock)
        self.cpu = cpu
    def shownotebook(self):
        return f"{super().check()}\nCPU {self.cpu}"

class Cloth(Product):
    def init(self,brand,name,price,stock,fabric):
        super().init(brand,name,price,stock)
        self.fabric = fabric
    def showcloth(self):
        return f"{super().check()}\nเนื้อผ้า {self.fabric}"

Mobile1 = Mobile("Samsung","s22 Ultra",45000,20,"Android")
Notebook1 = Notebook("Acer","Nitro5",23000,10,"ryzen7 5800H")
Cloth1 = Cloth("PAKAMAS","ผ้าขาวม้า",1200,120,"Cotton")
Mobile1.Edit("Stock")

print(f"{Mobile1.showmobile()}")