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
    def __init__(self, name, age, color,race) :
        super().__init__(name, age, color)
        self.race = race
    def showdog (self) :
        return f" สุนัขพันธุ์ {self.race} มี {super().show()}"
dog1 = Dog("สาริณี",3,"ขาว","ชิวาวา")
print(dog1.showdog())
