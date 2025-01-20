class Animal :
    def __init__(self, name,age,color) :
        self.name = name
        self.age = age
        self.color = color
    def show (self) :
        return f"ชื่อ {self.name} อายุ {self.age} ปี มีสี {self.color}"
 # amimali1 = Animal("สุพัดตา",2,"ดำ")
# print(amimali1.show())    

class Dog(Animal) :
    def bark(self) :
        return "โฮ่งๆ"
Dog1 = Dog("สาริณี",3,"ขาว")   
print(f"{Dog1.show()} สุนัขชื่อ {Dog1.name} ร้อง {Dog1.bark()}")
print(f"ข้อมูลชองหมาตัวที่1 {Dog1.show()}")